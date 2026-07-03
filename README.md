# MiniDrone Remote Controller

## Project Description

### English
This project provides a remote control application for a cheap mini-drone, allowing users to control its flight and view its video stream from a PC. It was developed by reverse-engineering the drone's communication protocols. The application features a graphical user interface (GUI) built with PySide6, a modular architecture for easy maintenance, and dynamic configuration of connection settings.

### Español
Este proyecto ofrece una aplicación de control remoto para un mini-dron económico, permitiendo a los usuarios controlar su vuelo y visualizar su transmisión de video desde una PC. Fue desarrollado mediante ingeniería inversa de los protocolos de comunicación del dron. La aplicación cuenta con una interfaz gráfica de usuario (GUI) construida con PySide6, una arquitectura modular para facilitar el mantenimiento y una configuración dinámica de los ajustes de conexión.

## How it Started

This project originated from an exploration into controlling a cheap mini-drone from a PC, inspired by the existence of a mobile application for the same drone. The initial script, which can be found in the `main.py` of the original project, involved understanding the drone's connections and ports. This repository represents a more formalized and professional version of that initial script, with a well-organized structure and a PySide6-based interface.

You can read more about the journey and the initial hacking process in my Medium article:
[El dron más barato hackeado](https://medium.com/@asaelriosalazar/el-dron-m%C3%A1s-barato-hackeado-4dad04831f78)

## Project Structure

```
MiniDrone-Remote Controller/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── drone_controller.py   # Handles UDP communication and drone commands
│   │   └── video_stream.py       # Manages video capture and streaming
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── drone_interface.ui    # UI definition (editable with Qt Designer)
│   │   └── main_window.py        # Main window class, loads UI and handles logic
│   ├── constants.py              # Global constants (IPs, ports, PWM values)
│   └── main.py                   # Main application entry point
├── README.md                     # Project description and instructions
└── requirements.txt              # (Optional) List of Python dependencies
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/MiniDrone-Remote-Controller.git
    cd MiniDrone-Remote-Controller
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install PySide6 opencv-python
    ```
    *(Optional: You might want to create a `requirements.txt` file with `pip freeze > requirements.txt`)*

## Running the Application

1.  **Ensure your virtual environment is activated.**
2.  **Run the main application script:**
    ```bash
    python main.py
    ```

## Using Qt Designer (Optional)

If you wish to modify the user interface:

1.  Open `src/gui/drone_interface.ui` with **Qt Designer**.
2.  Make your desired changes and save the `.ui` file.
3.  Since the application loads the `.ui` file directly, **no compilation step (`pyside6-uic`) is needed** unless you explicitly want to generate a `.py` file from the `.ui`. Just run `python main.py` to see your changes.

## Contribution

Feel free to fork the repository, open issues, or submit pull requests.

---
**Author:** Asael Rios Salazar
