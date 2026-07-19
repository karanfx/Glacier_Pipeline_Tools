# Glacier Pipeline Tools

**Figure:** Glacier Pipeline Tools launcher UI (v1.5.0). Glacier is a **VFX pipeline toolkit and project launcher** designed primarily for small studios and freelancers. It automates shot/task setup and software launching: Glacier connects to a Google Sheets API to fetch shot/task data, lists them in its launcher, and when a task is selected it creates the folder structure and opens the DCC software with all project settings (directories, environment variables, plugins, OTLs, etc.) pre-configured. The goal is to streamline production workflows: artists simply pick a shot from the UI and Glacier handles the rest (directory creation, loading plugins, etc.). The current version (v1.5.0) focuses on the main launcher and includes specialized tools for Houdini and Maya. Future features (asset auto-loading, client packaging, notifications, etc.) are planned.

**Repository:** [github.com/karanfx/Glacier_Pipeline_Tools](https://github.com/karanfx/Glacier_Pipeline_Tools) • **Demo video:** [YouTube – Glacier 1.5.0 Demo](https://youtu.be/o0MyRwAErkE?si=ZDDO3H-k9O9iU7pq)  

## Demo Overview
Watch our demonstration video here for an in-depth look at GLACIER's features.
<a href="http://www.youtube.com/watch?feature=player_embedded&v=o0MyRwAErkE
" target="_blank"><img src="http://img.youtube.com/vi/o0MyRwAErkE/0.jpg" 
alt="Glacier Tools 1.5.0 Demo" width="480" height="320" border="5" /></a>


## Quick-Start Checklist

- **Clone the repo:** `git clone https://github.com/karanfx/Glacier_Pipeline_Tools.git`  
- **Install dependencies:** `pip install -r requirements.txt` (Requires Python 3.x and pip)  
- **Configure Google Sheets:** Enable Sheets API in Google Cloud, obtain credentials (OAuth or service account JSON) and share your tracking Sheet with it  
- **Set up Glacier:** Edit the configuration (sheet ID, credential path, base project directory). If running locally, define required project path variables.  
- **Configure DCC apps:** Ensure Houdini/Maya (or other DCC) executables and required plugins are accessible  
- **Run Launcher:** `python qt_launcher.py` to start the Glacier UI  

## Installation & Setup

1. **Prerequisites:** Glacier is written in Python (3.x) and uses PySide/Qt for the UI. Install a compatible Python (≥3.7) and pip. You’ll also need a Google Cloud project with **Google Sheets API enabled**, a Google account, and [pip] installed.  
2. **Clone the repo:**  
   ```bash
   git clone https://github.com/karanfx/Glacier_Pipeline_Tools.git
   cd Glacier_Pipeline_Tools
   ```  
3. **Install Python packages:**  
   ```bash
   pip install -r requirements.txt
   ```  
   This will install Qt/PySide and Google Sheets client libraries.  
4. **Configure Google Sheets API:** In the Google Cloud Console, enable the **Google Sheets API**. Create credentials (OAuth client ID for desktop app, or a service account) and download the JSON key. Share your tracking spreadsheet (Shot/Task list) with the service account’s email or grant access via OAuth.  
5. **Update Glacier settings:** Create or edit a configuration file (e.g. `glacier_config.py` or environment variables) to include:
   ```python
   SHEET_ID = "your_google_sheet_id_here"
   GOOGLE_CRED_JSON = "/path/to/your/service_account.json"
   PROJECT_ROOT = "/path/to/project_folder"   # Base path for all project data
   ```
   *(Exact config names may vary; insert values as needed).*  
6. **Set environment/DCC paths:** If your DCC (Houdini, Maya, etc.) is not in the system PATH, you may need to set the executable path in your environment or in Glacier’s settings. Also set any pipeline environment variables (render license servers, etc.) if required for your studio.  
7. **Launch Glacier:** From the repo folder, run:  
   ```bash
   python qt_launcher.py
   ```  
   The Glacier launcher window will open and immediately fetch shot/task data from the Google Sheet.

## Usage Guide

### 1. Fetching Tasks

- On startup, Glacier connects to the configured Google Sheet and **fetches all shot/task entries**. The table/grid in the UI is automatically populated. This ensures that any updates made in the spreadsheet (new tasks, status changes, assignments) are reflected in real-time. 

- **Reload Tasks:** If production updates the sheet while you are running Glacier (e.g. they add a task or reassign a shot), click the **Reload Tasks** button (🔄) or restart the launcher. Glacier will re-query the sheet and update the list. Any new tasks will now appear, and their folder structures will be created on your workstation.

### 2. Selecting a Shot/Task

- **Table and Dropdown:** Choose your desired working shot in one of two ways: (a) click the row in the table, or (b) select it from the drop-down menu above. Both methods filter the list for quick access.  

- **Manual Path (Optional):** If you need to open an *untracked* or R&D shot not yet in the sheet, use the *Manual Path* option. Browse to the desired project folder or scene file. This lets you use Glacier’s launcher for tasks outside the Google Sheet workflow.  

- When a shot is selected, Glacier will immediately **create the standard folder structure** for that shot on disk (if not already present). For example, it may create subfolders for `animation`, `lighting`, `cache`, `render`, etc., under the base project directory.

### 3. Launching DCC Software

- In the launcher UI, click the button for the DCC application you want (e.g. **Houdini** or **Maya**). Glacier will then:
  - **Set the project environment:** All relevant environment variables (project root, shot name, etc.) are set so the DCC knows which project to work on.  
  - **Load plugins/OTLs:** Any required plugins, Python packages, or Houdini OTLs for that shot are loaded automatically. This ensures the DCC is fully configured for the task.  
  - **Open the project:** If the software supports a scene file (or a project file), Glacier can open it directly. Otherwise, it just launches the app into the correct working directory.  

  For example:  
  ```bash
  # (This is done internally by the GUI. Shown here conceptually.)
  import subprocess
  subprocess.Popen(["houdini", "-proj", "/projects/MyMovie/shot010"])
  ```  
  After launch, the DCC will be ready to work on the selected shot.  

### 4. Version Management

- The Launcher also provides version control for each DCC. Click **Launch Version** to see a list of previous versions saved for that task/DCC (e.g. `anim_v001.hip`, `anim_v002.hip`). Select one to open that specific version in the DCC. This lets you review or continue older work easily. Glacier automatically tracks versions when you save from within the DCC.  

### 5. Houdini & Maya Tools

Once your project is launched in Houdini or Maya, additional Glacier tools become available (usually in a menu or shelf):

- **Houdini Tools:** Glacier includes several pipeline scripts inside Houdini. For example:
  - **Asset Importer:** With one click (“Build Scene”), import published assets or geometry from other departments into your current Houdini scene.
  - **Object Merge Tool:** Select nodes in your scene and use this to quickly create references to them at the `/obj/` level. Simplifies scene linking.
  - **Quick Render Setup:** Auto-generate a Mantra/Karma ROP with the correct output paths and settings for this shot, saving manual setup time.
  - **Output Dir Setter:** Instantly set the file output paths of your ROPs and caches to the correct directories for this shot.
  - **Cache Manager:** A small interface for managing simulation/geometry caches. You can **Clean Up** (remove old caches) or **Collect Cache** (copy current caches into the publish folder) with one click.
  - **Publisher:** When assets are ready for handoff (e.g. for lighting or compositing), use the publisher tool to organize and move the files into the central `lib/` directory. It enforces naming conventions and file placement.
  - **Notifier:** Optionally send an email (or Discord message) alert when a task (like a render or cache bake) completes. (This is configured per-task.)

- **Maya Tools:** Glacier offers similar helpers in Maya:
  - **Asset Importer:** Load published Maya scenes or exported geometry into the current scene with a custom import script.
  - **Turntable Tool:** Automate creation of turntable playblasts. The tool sets up a camera circling the selected objects and outputs an image sequence or video.

*(Nuke tools are mentioned as upcoming on the website, and may be added later.)* 

### 6. Environment Variables and Local Settings

- Glacier automatically sets environment variables needed by the project (like `SHOT_NAME`, `PROJECT_PATH`, `OUTPUT_PATH`, etc.) when launching the DCC. If you are working **locally** (not on the studio server), you may need to define some base paths manually. The launcher UI provides fields to override defaults (e.g. base project folder on your machine). 

### 7. Example Commands

- **Start Launcher:**  
  ```bash
  cd Glacier_Pipeline_Tools
  python qt_launcher.py
  ```  
- **Reload tasks manually (in case of sheet update):** Click the “Reload Tasks” button in the UI (🔄).  

- **Troubleshooting:** If no tasks appear, check your Google Sheets credentials and sheet ID. Ensure the sheet’s format (column headers) matches what Glacier expects. If a DCC fails to launch, verify its executable path and project folder permissions. *(Since specifics vary by studio setup, details may be *unspecified*.)*

## Features Overview

| **Component**       | **Key Features**                                                                                | **Description**                                                                                                                                                    |
|---------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Glacier Launcher**| • Google Sheets integration (auto-fetch shot data)<br>• Dynamic task list (live updates)<br>• Automated task/shot folder creation<br>• Direct DCC launch with env and plugins<br>• Version management (previous saves) | The core UI that ties everything together. Fetches tasks from Google Sheets and displays them; lets artists pick a shot; auto-generates the project folder structure; and launches the chosen DCC application with all settings pre-configured. Tracks file versions for easy recall. |
| **Houdini Tools**   | • Asset Importer<br>• Object Merge<br>• Quick Render Setup<br>• Output Directory Setter<br>• Cache Manager (Clean/Collect)<br>• Publisher (lib directory)<br>• Notifier (email alerts) | A suite of Houdini scripts for common tasks: importing assets from other departments; merging node groups; setting up render ROPs; fixing output paths; managing caches; and publishing assets to the studio library. Also includes an email notification tool for task completion. |
| **Maya Tools**      | • Asset Importer<br>• Turntable Tool                                                                        | Pipeline helpers for Maya: load published assets quickly, and automate turntable playblast creation for selected models. Additional Maya-specific utilities (e.g. rigging support) may be added in future. |
| **Nuke Tools**      | *(Planned)*<br>                                                                       | Nuke-specific tools are planned for a future release (features may include camera/geometry import, render/pass setups, etc.).                                    |

## Roadmap and Future Features

The developer has outlined an **ambitious roadmap** for Glacier. Planned enhancements include:

- **Automatic Dependencies:** On launch, automatically import/reference all assets (geometry, textures, caches) needed for the shot.  
- **Client Packaging Tool:** A separate export tool to gather final renders, caches, and other deliverables into a single “publish” folder or archive for client delivery.  
- **Expanded DCC Tools:** More specialized tools for each DCC (e.g. additional Maya rigging scripts, Nuke compositing helpers) based on artist feedback.  
- **Alerts & Notifications:** Integrate email/Discord alerts for shot status changes and task completions.  
- **Review Integration:** A review module to sync artist notes/annotations from review sessions directly with the launcher tasks.  

```mermaid
flowchart LR
    A[Google Sheet (Project Data)] --> B[Glacier Launcher fetches tasks]
    B --> C[User selects shot/task]
    C --> D[Glacier creates directory structure]
    D --> E[Launch DCC (Houdini/Maya) with project env]
    E --> F[DCC loads scene, plugins, work begins]
    B --> G[Reload Tasks (sync updates)]
```
*Flowchart: Glacier launch workflow, from sheet data to DCC.*

## Troubleshooting

- **No tasks appearing:** Verify the Google Sheet ID and that your credentials JSON is correct. Check that the sheet’s columns match Glacier’s expected format. Confirm the service account (or OAuth user) has permission to read the sheet.  
- **Folder creation fails:** Ensure the `PROJECT_ROOT` path is valid on your machine and you have write permissions. If you changed base directories, check Glacier’s local path variables.  
- **DCC won’t launch:** Confirm the DCC executable path is correct and in PATH (or set in config). Check that the environment variables (licenses, etc.) are set up properly. Try running the DCC manually from that path to rule out permissions.  
- **Missing plugins/OTLs:** If specific plugins aren’t loading, ensure they are installed in the expected location and that Glacier’s config points to them. You may need to adjust the plugin search paths.  

*(Because studio setups vary, many config details may be unspecified. If issues persist, contact support.)*

## Contribution & Support

Contributions and feedback are welcome! If you encounter bugs or have feature requests, please use the [GitHub Issues](https://github.com/karanfx/Glacier_Pipeline_Tools/issues) page or submit a pull request. (A contributor license or formal process is not specified; please assume any code you contribute will be under the project’s terms.) 

For questions or support, you can contact the developer directly at **contact@karanmirajkar.com**. Thank you for using Glacier – your suggestions help shape future features.

