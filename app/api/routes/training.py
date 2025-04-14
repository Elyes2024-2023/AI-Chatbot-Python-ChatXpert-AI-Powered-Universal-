"""
Training routes for ChatXpert
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import json

from app.core.database import mongodb
from app.core.security import get_current_user

# Done by ELYES
router = APIRouter()

class TrainingData(BaseModel):
    # Done by ELYES
    intent: str
    patterns: List[str]
    responses: List[str]

class TrainingStatus(BaseModel):
    # Done by ELYES
    status: str
    progress: float
    last_updated: datetime
    metrics: Optional[dict] = None

@router.post("/data", response_model=TrainingData)
async def add_training_data(
    data: TrainingData,
    current_user = Depends(get_current_user)
):
    # Done by ELYES
    try:
        # Store training data in MongoDB
        await mongodb.training_data.insert_one({
            "intent": data.intent,
            "patterns": data.patterns,
            "responses": data.responses,
            "created_by": current_user.username,
            "created_at": datetime.now()
        })
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def upload_training_file(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user)
):
    # Done by ELYES
    try:
        content = await file.read()
        data = json.loads(content)
        
        # Validate and store training data
        for item in data:
            if not all(k in item for k in ["intent", "patterns", "responses"]):
                raise HTTPException(
                    status_code=400,
                    detail="Invalid training data format"
                )
            
            await mongodb.training_data.insert_one({
                "intent": item["intent"],
                "patterns": item["patterns"],
                "responses": item["responses"],
                "created_by": current_user.username,
                "created_at": datetime.now()
            })
        
        return {"message": "Training data uploaded successfully"}
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON format"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/train")
async def train_model(current_user = Depends(get_current_user)):
    # Done by ELYES
    try:
        # Create training job
        job_id = await mongodb.training_jobs.insert_one({
            "status": "pending",
            "progress": 0.0,
            "created_by": current_user.username,
            "created_at": datetime.now()
        })
        
        # TODO: Implement actual model training logic
        # This would typically involve:
        # 1. Fetching training data
        # 2. Preprocessing
        # 3. Training the model
        # 4. Saving the model
        # 5. Updating job status
        
        return {
            "message": "Training job started",
            "job_id": str(job_id.inserted_id)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{job_id}", response_model=TrainingStatus)
async def get_training_status(
    job_id: str,
    current_user = Depends(get_current_user)
):
    # Done by ELYES
    try:
        job = await mongodb.training_jobs.find_one({"_id": job_id})
        if not job:
            raise HTTPException(status_code=404, detail="Training job not found")
        
        return TrainingStatus(
            status=job["status"],
            progress=job["progress"],
            last_updated=job.get("updated_at", job["created_at"]),
            metrics=job.get("metrics")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 