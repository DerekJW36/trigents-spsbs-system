from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from models.vehicle import Vehicle, PartSearchRequest
from inventory.napa_scraper import NapaScraper
from tools.payments import generate_payment_link_tool
from tools.web_comparison import get_web_comparison_link_tool
import os
import uvicorn
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Auto Parts Receptionist API")

# Initialize our Demo Inventory Provider
inventory_provider = NapaScraper()

class VapiToolCallRequest(BaseModel):
    message: dict

@app.get("/")
def read_root():
    return {"message": "AI Auto Parts Receptionist API is running."}

@app.post("/vapi-webhook")
async def vapi_webhook(request: Request):
    """
    Endpoint for Vapi.ai (or similar voice providers) to call custom tools.
    The AI will send tool call requests here.
    """
    payload = await request.json()
    logger.info(f"Received webhook: {payload}")
    
    # Vapi sends messages of type toolCalls
    message = payload.get("message", {})
    if message.get("type") == "toolCalls":
        tool_calls = message.get("toolCalls", [])
        results = []
        for call in tool_calls:
            function_name = call.get("function", {}).get("name")
            arguments = call.get("function", {}).get("arguments", {})
            call_id = call.get("id")
            
            if function_name == "search_inventory":
                # Extract arguments provided by the AI
                vehicle_data = arguments.get("vehicle", {})
                part_name = arguments.get("part_name")
                
                try:
                    vehicle = Vehicle(**vehicle_data)
                    # Use our modular inventory provider
                    parts_found = inventory_provider.search_part(vehicle, part_name)
                    
                    results.append({
                        "toolCallId": call_id,
                        "result": {
                            "status": "success",
                            "parts": parts_found
                        }
                    })
                except Exception as e:
                    logger.error(f"Error searching part: {e}")
                    results.append({
                        "toolCallId": call_id,
                        "result": {
                            "status": "error",
                            "error": str(e)
                        }
                    })
            elif function_name == "generate_payment_link":
                part_name = arguments.get("part_name")
                price_dollars = float(arguments.get("price_dollars", 0.0))
                customer_phone = arguments.get("customer_phone")
                
                try:
                    result = generate_payment_link_tool(part_name, price_dollars, customer_phone)
                    results.append({
                        "toolCallId": call_id,
                        "result": result
                    })
                except Exception as e:
                    logger.error(f"Error generating payment link: {e}")
                    results.append({
                        "toolCallId": call_id,
                        "result": {
                            "status": "error",
                            "error": str(e)
                        }
                    })
            elif function_name == "get_web_comparison_link":
                sku = arguments.get("sku")
                store_id = arguments.get("store_id", "default")
                
                try:
                    result = get_web_comparison_link_tool(sku, store_id)
                    results.append({
                        "toolCallId": call_id,
                        "result": result
                    })
                except Exception as e:
                    logger.error(f"Error generating comparison link: {e}")
                    results.append({
                        "toolCallId": call_id,
                        "result": {
                            "status": "error",
                            "error": str(e)
                        }
                    })
                    
        return {
            "results": results
        }
        
    return {"status": "ignored"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
