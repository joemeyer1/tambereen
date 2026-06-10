
![movement to sound diagram](https://github.com/user-attachments/assets/a0d94ffa-2e63-4f2e-98be-e40fbcdb63e6)


Tambereen is a movement sonification system (i.e. a digital musical instrument) for synthesizing novel timbres consisting of two primary components:

1. An autoencoder-based unsupervised learning algorithm for mapping movements to sounds, enabling you to synthesize audio from your movements

2. Latent Novelification (LN), a network bending method for interactively transforming movement-to-sound mappings, enabling you to "tune" the sound space you're interacting with


Tambereen requires no specialized hardware, using computer vision to extract real-time pose data from video feed of your movements (captured by default via your laptop's built-in camera), and lightweight ML algorithms to map your movements to sound (meaning you don't need a powerful computer to run it). Its unsupervised approach enables it to learn mappings that "just work", from your custom movements to a set of sounds you may curate, without you needing to demonstrate many individual paired movement-sound examples or risk a randomized mapping that may not yield a coherent interaction space. Its LN component enables you to interactively change the sounds your movements map to, and explore new regions of timbre.


To set up (on a Mac):

1. Download this GitHub repository https://github.com/joemeyer1/tambereen

    If you aren't familiar with Git or Python, do the following:
    
    - Navigate to https://github.com/joemeyer1/tambereen in your web browser
    - Click the green "Code" tab in the upper right corner of the web page
    - Click "Download Zip"
    - After repository has downloaded, go to your "Downloads" folder and double-click the zip file

2. Optional, but recommended -- To use a default "musicnet", "percussion", or "VCTK" RAVE model with Max integration, download the corresponding standalone Tambereen interface app from my Drive folder: https://drive.google.com/drive/folders/1IZOI1tm24UPqegra14_TkFS1Drl81CEU?usp=sharing , drag it to the `interfaces` folder of this repo, then unzip it by double-clicking on it.

    Advanced users: To use Tambereen Max interface for custom RAVE models...
    
    1. Download Max MSP (it has a free trial version which allows you to use and modify the .maxpat interfaces): https://cycling74.com/downloads 
    2. Download nn_tilde (source: https://github.com/acids-ircam/nn_tilde , troubleshooting: https://github.com/acids-ircam/nn_tilde/issues/92#issuecomment-3438803980 )
    3. Add your custom RAVE model to this repo's `interfaces` folder
    4. Open `interfaces/tambereen_interface_musicnet.maxpat` in Max MSP for use as a template patch. Replace the text "musicnet" in the "nn~ musicnet decode" box with your custom RAVE filename (excluding filename extension), and replace the text "16" in the "mc.unpack~ 16" box with the number of latent dimensions your custom RAVE model uses.

    [If you don't want to use Max, set the `AudioMovementProjectorSettings.PYTHON_PLAY_AUDIO` variable in run_settings.py to `True`, and `AudioMovementProjectorSettings.AUDIO_FRAMES_PER_CHUNK` in `run_settings.py` to `10`, and the program will use python to play the audio instead of using Max. But Warning: If you use python instead of Max to play the audio, the live audio you hear during interaction -- though not the audio recorded to file -- will be choppy and delayed, and you won't be able to use the novelification interface which is implemented in Max.]

3. Open "Terminal" application (it is in your "Applications" folder in "Finder")

4. Navigate to the downloaded GitHub folder in Terminal

    If you aren't familiar with Git or Python, do the following:
    
    - Type ```cd Downloads/tambereen-main``` into Terminal window, then press "Enter" key
    
5. Copy the following block of commands into Terminal window, then press "Enter" key:

    ```
    command -v brew &>/dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    brew install python@3.9

    python3.9 -m venv env
   
    source env/bin/activate
   
    python install_requirements.py
    ```

6. Now the software is installed. To run it:
    - Type ```python main.py``` into Terminal window, then press "Enter" key. 


If you aren't familiar with Git or Python, do the following:

- Once the software is installed, you can run it any time by opening "Terminal" application, copying and pasting the following code block into the Terminal window, then pressing "Enter" key:

    ```
    cd
    
    cd Downloads/tambereen-main
  
    source env/bin/activate
  
    python main.py
    ```

Note: You can modify run settings by changing variables of the Settings classes in "run_settings.py". 

Training Flow for Tambereen:
    When Tambereen is run, it will initially do some set-up work (e.g. preparing audio models and audio training embeddings), which may take a moment. Then it will display camera feed (i.e. from your computer's built-in camera) in a new window, and you may demonstrate the movements you want to use to interact with it. When you are done demonstrating your movements, press "q" on your keyboard and the model will train mappings from your demonstrated movements to the audio specified by the AUDIO_TRAINING_DATA_PATH variable in "run_settings.py". When the model is done training, it will save, so you can load and interact with it later. Then the program will open the Tambereen Max interface (unless PYTHON_PLAY_AUDIO is set to "True"), and open a window showing your camera feed. Press the big button labeled "Start / Stop" in the lower left corner of the Max interface to enable audio and hear your sonified movements in real time. When you are done with your interaction, press the "Start / Stop" button in the Max interface, then navigate to the "Terminal" window running the program and press "ctrl-c" on your keyboard. The program will terminate and if you indicate in "run_settings.py" to save your interaction data, it will be written to "output_data_runs" folder.


File structure:

    install_requirements.py
        Script for automatically installing Tambereen requirements

    run_settings.py
        User settings for Tambereen runs
    
    interfaces
        Max patches for Tambereen interaction, including default and finegrained LN controls (interface path is a modifiable user setting). Interfaces are model-specific, because they must load the correct audio model and match input dimensionality to the model's latent space.

    audio_training_data
        Folders of training data (path used for training can be specified in run_settings.py)

    output_data_runs
        Stores all data generated by Tambereen runs, with each run’s logged data in a unique index directory

    main.py
        Calls main script to run Tambereen (by default, calls src.scripts.run_tambereen.py)

    src
        model_managers
            Manage saving and loading models

        projectors
            Project input data into an output space (transforming the data by some function)

        scripts
            Scripts for using or training models

        streamers
            Read data, move it between different processes (for concurrency), output audio (streaming audio embeddings to Max or decoding and playing them directly via Python)

        time_chunks
            Containers for data (synchronizing frames in different modalities across chunks of time)

        trainers
            Train models

        utils.py
            Defines utility functions

    tests
        Unit tests


Acknowledgments:

Thank you to Shuoyang Jasper Zheng for helping with early stages of Max integration (including providing the initial RAVE decoder Max patch), and to Ashley Noel-Hirst for helping to convert Max patches into standalone app interfaces.
