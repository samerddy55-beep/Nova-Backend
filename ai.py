import time

from config import config


class NovaAI:
    """
    Nova AI Engine

    حاليًا هذه طبقة محرك مستقلة.
    لاحقًا سنربطها بالنموذج المحلي الحقيقي
    دون تغيير واجهة الـAPI.
    """

    def __init__(self):
        self.engine = config.AI_ENGINE
        self.model = config.AI_MODEL

    def status(self):
        return {
            "engine": self.engine,
            "model": self.model,
            "status": "ready"
        }

    def generate(self, message: str):
        start = time.time()

        # Placeholder مؤقت للمحرك.
        # لن نضع نموذجًا وهميًا على أنه AI حقيقي.
        response = (
            "Nova AI Engine is connected. "
            "The local model has not been loaded yet. "
            "Your request was received successfully."
        )

        elapsed = round(
            time.time() - start,
            4
        )

        return {
            "success": True,
            "model": self.model,
            "response": response,
            "processing_time": elapsed
        }


nova_ai = NovaAI()
