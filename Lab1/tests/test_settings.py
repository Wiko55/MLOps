from settings import Settings


def test_settings_loads_values():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "mlops-test"
    assert settings.api_key == "test_key"
