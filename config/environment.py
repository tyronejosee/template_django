"""Enviroments."""

import environ

# ! TODO: Refactor
env = environ.Env()
environ.Env.read_env(".env")


# Example: "local", "testing", "production"
ENVIRONMENT = env("ENVIRONMENT")

SETTINGS_MODULE = "config.settings.local"

if ENVIRONMENT == "local":
    SETTINGS_MODULE = "config.settings.local"
if ENVIRONMENT == "testing":
    SETTINGS_MODULE = "config.settings.testing"
if ENVIRONMENT == "production":
    SETTINGS_MODULE = "config.settings.production"
