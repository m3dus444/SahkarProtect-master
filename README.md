# SahkarProtect-master
IDE : Pycharm VCS (git m3du444 by SSH)

This is a project to handle downloaded files via chrome and flash drives to avoid ransomware / malwares. 
Files with unreliable extensions (configure that in extensions.py file)  are dumped of Download folder or Flash drive to be dynamically analysed by the API https://hybrid-analysis.com to complete SMA and DMA.
Chrome is set to org. mod to disable users moving their download folder. This is done by setting up organisation policies (your personal configuration here as well) and write registry. This needs Admin privileges at first use.

Get a DB of Malware here : https://github.com/Endermanch/MalwareDatabase

To install Sakhar protect, please follow instructions bellow : 
-get latest Python version : Python 3.9.5. 
-move to `/SakharProtect-master/`
-install requirements : `python -m pip install requirements.txt`.  
-move to `/SakharProtect-matser/app` and run : `python ./main.py` with Admin privilege.
-Wait for setting up chrome to org mode and registry keys.
-re run `python ./main.py` without admin privilege.

You're now good to go ! Every download should be crypted et gone for analyse.
Wait for result and check console.
