from pydantic_core import Url
from app.dto.user import UserRequest
from app.repository.memory import MemoryRepository
from app.use_case.user import UserAddUseCase


def test_user_add_use_case():
    data = {
        "name": "test",
        "email": "me@test.com",
        "avatar": "https://s3.amazon.com/avatar.jpg",
    }

    repo = MemoryRepository()
    case = UserAddUseCase(repo)
    user = UserRequest(**data)

    result = case.execute(user).to_dict()

    assert len(result) == 4
    assert result["id"] == "1"
    assert result["name"] == data["name"]
    assert result["email"] == data["email"]
    assert result["avatar"] == Url(data["avatar"])
