import os
import configparser

def cargar_configuracion():
    env = os.getenv("APP_ENV", "dev")

    if env == "test":
        config_file = "config_test.ini"
    elif env == "prod":
        config_file = "config_prod.ini"
    else:
        config_file = "config_dev.ini"
        env = "dev"

    config = configparser.ConfigParser()
    config.read(config_file, encoding="utf-8")

    return env, config

def main():
    env, config = cargar_configuracion()

    app_name = config["app"]["name"]
    message = config["app"]["message"]
    debug = config["app"].getboolean("debug")
    version = config["app"].get("version", "0.1.0")
    log_level = config["app"].get("log_level", "NOTSET")

    print("==============================")
    print(f"Aplicación : {app_name}")
    print(f"Entorno    : {env}")
    print(f"Versión    : {version}")
    print(f"Mensaje    : {message}")
    print(f"Debug      : {debug}")
    print(f"Log level  : {log_level}")
    print("==============================")

if __name__ == "__main__":
    main()
