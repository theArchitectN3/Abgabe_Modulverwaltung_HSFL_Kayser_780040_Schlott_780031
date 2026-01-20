import unittest
from unittest.mock import MagicMock
from app.application.service import ModulWorkflowService
from app.domain import models, schemas
from fastapi import HTTPException

class TestModulWorkflow(unittest.TestCase):
    """
    Tests business logic of workflow (Unit-Testing).
    Uses mocks to isolate database dependencies.
    """

    def setUp(self):
        # Mocking the database session and repository
        self.mock_db = MagicMock()
        self.service = ModulWorkflowService(self.mock_db)
        self.service.repository = MagicMock()

    def test_submit_success(self):
        """
        Test: Valid module submission.
        Expectation: Status changes to REVIEW_COORDINATOR.
        """
        # Arrange: Create a valid module in DRAFT status
        mock_modul = models.Module(
            id=1, 
            title="Software Engineering", 
            ects=5, 
            description="Content...", 
            status="DRAFT"
        )
        # Setup mock returns
        self.service.repository.get_module_by_id.return_value = mock_modul
        self.service.repository.update_status.return_value = mock_modul

        # Act: Call the submit method
        self.service.submit_module(1)

        # Assert: Verify repository was called with correct new status
        self.service.repository.update_status.assert_called_with(1, "REVIEW_COORDINATOR")

    def test_submit_fail_missing_fields(self):
        """
        Test: Submit module with missing description.
        Expectation: HTTPException (400).
        """
        # Arrange: Module with empty description
        mock_modul = models.Module(
            id=2, 
            title="Incomplete Module", 
            ects=5, 
            description="", # Empty!
            status="DRAFT"
        )
        self.service.repository.get_module_by_id.return_value = mock_modul

        # Act & Assert: Expect error
        with self.assertRaises(HTTPException):
            self.service.submit_module(2)

    def test_submit_fail_wrong_status(self):
        """
        Test: Submit already released module.
        Expectation: HTTPException (400).
        """
        # Arrange: Module is already RELEASED
        mock_modul = models.Module(id=3, status="RELEASED")
        self.service.repository.get_module_by_id.return_value = mock_modul

        # Act & Assert
        with self.assertRaises(HTTPException):
            self.service.submit_module(3)

if __name__ == '__main__':
    unittest.main()