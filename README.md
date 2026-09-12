<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />

# SCREAM LAPTOP 🎯

## Basic Details
### Team Name: The Dua gng

### Team Members
- Team Lead: SHREERAM V - Ahalia School of Engineering and Technology
- Member 2: KARANJITH KJ - Ahalia School of Engineering and Technology

### Project Description
SCREAM LAPTOP (Scream-to-See / S2S) is the ultimate high-stress human-computer interface. By default, your Linux PC assumes you are unconscious, compromised, or absent, maintaining a 100% pitch-black desktop overlay. The only way to reveal your display and get work done is by continuously screaming into your microphone at maximum vocal capacity.

### 🎭 The Problem (that doesn't exist)
Desktop environments are designed around the flawed assumption that human lungs and computer monitors should operate independently. If your CPU fans have to spin at maximum RPM just to keep your system running, it is fundamentally unfair that your lungs get to sit there doing low-effort, silent breathing. Silent compute power is an unaccountable waste of human respiratory capacity.

### 💡 The Solution (that nobody asked for)
**Scream-to-See (S2S)**: An ultra-smooth, audio-reactive desktop overlay that forces human oxygen consumption to scale directly with screen output.

By default, your monitor assumes your lungs are lazy and maintains a 100% pitch-black overlay. The only way to earn desktop pixels is to continuously match your system's thermal load by screaming into your microphone at maximum vocal power.

- **Quiet Breathing / Normal Speech**: 100% total darkness.
- **Moderate Shouting**: A pathetic 12% desktop visibility.
- **Full-Throated Bloodcurdling Scream**: Smoothly forces back the void, granting access to your open windows.
- **Running Out of Breath?** The dark void glides back over your monitor in seconds.

Powered by dual-stage exponential moving average (EMA) motion filters, non-linear dynamic range mapping, and dynamic ALSA audio capture on Arch/EndeavourOS.

---

## Technical Details

### Technologies/Components Used
For Software:
- **Languages used**: Python 3
- **Libraries used**: `PyAudio` (real-time microphone input stream), `NumPy` (RMS volume & array processing)
- **Tools used**: `dzen2` (lightweight X11 overlay renderer), `xrandr` (dynamic resolution detection), `Linux / Bash`

---

### Implementation

#### Installation

##### 1. System Dependencies (Linux / X11)

**Debian / Ubuntu / Pop!_OS:**
```bash
sudo apt-get update
sudo apt-get install dzen2 x11-xserver-utils portaudio19-dev
```

**Arch Linux / Manjaro:**
```bash
sudo pacman -S dzen2 xorg-xrandr portaudio
```

##### 2. Clone Repository & Setup Virtual Environment
```bash
# Clone repository from GitHub
git clone https://github.com/KStupid/useless_project_temp.git
cd useless_project_temp

# Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

#### Run
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Run the scream overlay
python screen15.py
```

---

### Project Documentation

#### Screenshots

![Partial Desktop Visibility](doc/Screenshot_of_the_project.png)
*1. Partial desktop visibility during moderate volume/shouting.*

![Full Visibility When Screaming](doc/image.png)
*2. Desktop completely revealed when screaming at maximum capacity.*

![Restored View After Stopping Code](doc/image%20copy.png)
*3. Desktop view fully restored after exiting the application.*

#### Diagrams
```
+-------------------+      +-------------------+      +-------------------+      +-------------------+
|  Microphone Input | ---> | RMS Volume Calc   | ---> | Exponential Curve | ---> |  dzen2 Black Out  |
|  (PyAudio Stream) |      | (NumPy Array Math)|      | & Alpha Smoothing |      |  Screen Overlay   |
+-------------------+      +-------------------+      +-------------------+      +-------------------+
```
*Workflow: Audio captured -> RMS computed -> Smoothing & quantization -> Dynamic `dzen2` width update.*

---

### Project Demo

#### Video
[Watch Project Demo Video](doc/Screencast_20260912_075946.webm)
*Demonstration of screen opening as sound levels rise and returning to black when quiet.*

---

## Team Contributions
- **SHREERAM V**: Idea generation and planning.
- **KARANJITH KJ**: Coding, bug testing, and implementation.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)
