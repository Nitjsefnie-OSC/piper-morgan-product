from abc import ABC, abstractmethod
from typing import Optional

from services.domain.models import AnalysisResult


class BaseAnalyzer(ABC):
    @abstractmethod
    async def analyze(self, file_path: str, *, user_id: Optional[str], **kwargs) -> AnalysisResult:
        """#2131: the acting principal picks the provider; None = a system call."""
        pass
