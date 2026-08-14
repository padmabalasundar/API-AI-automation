import pytest
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, NotFoundError
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# ---------------------------------------------------------
# Define Expected Schema using Pydantic
# ---------------------------------------------------------
class UserProfile(BaseModel):
    name: str
    age: int
    is_active: bool
    skills: list[str] = Field(description="List of technical skills")

# ---------------------------------------------------------
# Pytest Fixture: Initializes the client for re-use across tests
# ---------------------------------------------------------
@pytest.fixture
def api_client():
    return OpenAI()


# ---------------------------------------------------------
# 1. POSITIVE TEST: Normal valid request
# ---------------------------------------------------------
def test_valid_chat_completion(api_client):
    response = api_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Reply with 'OK'."}],
        temperature=0.0
    )
    
    # Assertions
    assert response.choices[0].message.content is not None
    assert "ok" in response.choices[0].message.content.lower()
    assert response.usage.total_tokens > 0


# ---------------------------------------------------------
# 2. NEGATIVE TEST: Invalid Model Name (Error Handling)
# ---------------------------------------------------------
def test_invalid_model_throws_not_found_error(api_client):
    # Catch NotFoundError (404) instead of BadRequestError
    with pytest.raises(NotFoundError) as exc_info:
        api_client.chat.completions.create(
            model="non-existent-model-xyz",
            messages=[{"role": "user", "content": "Hello"}]
        )
    
    # Assert that the status code is 404 and error message mentions 'model'
    assert exc_info.value.status_code == 404
    assert "model" in str(exc_info.value).lower()


# ---------------------------------------------------------
# 3. NEGATIVE TEST: Invalid API Key Authentication
# ---------------------------------------------------------
def test_invalid_api_key_throws_authentication_error():
    # Initialize a client with an intentionally wrong key
    bad_client = OpenAI(api_key="sk-invalid-fake-key-12345")
    
    with pytest.raises(AuthenticationError) as exc_info:
        bad_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello"}]
        )
    
    assert exc_info.value.status_code == 401

# ---------------------------------------------------------
# 4. STRUCTURED OUTPUT TEST: Validating Schema & Types
# ---------------------------------------------------------
def test_structured_json_output(api_client):
    prompt_data = "Extract user info: Alex Smith is a 29 year old active developer skilled in Python, SQL, and Docker."

    # Use client.beta.chat.completions.parse to enforce Pydantic schema output
    response = api_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract structured user details from the provided text."},
            {"role": "user", "content": prompt_data}
        ],
        response_format=UserProfile
    )

    # 1. Extract parsed object directly (already validated by Pydantic)
    user: UserProfile = response.choices[0].message.parsed

    # 2. Automated Assertions on Data Types and Contents
    assert isinstance(user, UserProfile), "Response should be an instance of UserProfile"
    assert user.name == "Alex Smith"
    assert user.age == 29
    assert user.is_active is True
    assert isinstance(user.skills, list)
    assert len(user.skills) == 3
    assert "Python" in user.skills