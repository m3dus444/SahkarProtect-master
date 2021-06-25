from werkzeug.utils import secure_filename
import subprocess
import json
import os
import time


UPLOAD_FOLDER = "./uploadServer/"
CMD_BASE = "python ./VxAPI/vxapi.py"
ARGUMENTS = "--no-share-third-party 1 --allow-community-access 0"


def execute_analysis(function_name, url=None, filename=None, root=None):
    if (function_name == "quick_scan_file" or function_name == "sandbox_file"):
        path = UPLOAD_FOLDER + filename
        result = globals()[function_name](path)
    else:
        result = globals()[function_name](url)
        print(url)
    if (result == "malicious" or result == "suspicious" or result == "timeout exceeded"):
        return 1
    return 0


def quick_scan_url(url):
    cmd_arguments = " scan_url_for_analysis " + ARGUMENTS + " " + \
        url + " scan_urlscanio"
    return executeScan(cmd_arguments)


def sandbox_url(url):
    cmd_arguments = " submit_url_for_analysis " + ARGUMENTS + " " + \
        url + " 120"
    return executeSandbox(cmd_arguments)


def quick_scan_url_file(url_file):
    cmd_arguments = " scan_url_to_file " + ARGUMENTS + " " + \
        url_file + " scan_metadefender"
    return executeScan(cmd_arguments)


def sandbox_url_file(url_file):
    cmd_arguments = " submit_url_to_file " + ARGUMENTS + " " + \
        url_file + " 120"
    return executeSandbox(cmd_arguments)


def quick_scan_file(path):
    cmd_arguments = " scan_file " + ARGUMENTS + " " + \
        path + " scan_metadefender"
    result = executeScan(cmd_arguments)
    # os.remove(path)
    return result


def sandbox_file(path):
    cmd_arguments = " submit_file " + ARGUMENTS + " " + \
        path + " 120"
    verdict = executeSandbox(cmd_arguments)
    # os.remove(path)
    return verdict


def executeScan(cmd_arguments):
    cmd = CMD_BASE + cmd_arguments
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    print(stdout)
    print(stderr)
    scan_id = json.loads(stdout)["id"]
    print(scan_id)
    job_done = False
    timeout = 0
    while (job_done is False and timeout < 15):
        time.sleep(5)
        scan_result = getScanResult(scan_id)
        if (timeout == 0):
            time.sleep(2)
        if (scan_result != "in-queue"):
            job_done = True
        timeout += 1
    if (timeout >= 15):
        return "timeout exceeded"
    return scan_result


def executeSandbox(cmd_arguments):
    cmd = CMD_BASE + cmd_arguments
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    print(stdout)
    print(stderr)
    job_id = json.loads(stdout)["job_id"]
    job_done = False
    timeout = 0
    while (job_done is False and timeout < 40):
        time.sleep(15)
        if (getSandboxState(job_id)):
            job_done = True
        timeout += 1
    if (timeout >= 5):
        return "timeout exceeded"
    return getSandboxSummary(job_id)


def getSandboxState(job_id):
    cmd = CMD_BASE + " report_get_state " + job_id
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    status = json.loads(stdout)["state"]
    return status == "SUCCESS"


def getSandboxSummary(job_id):
    cmd = CMD_BASE + " report_get_summary " + job_id
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    verdict = json.loads(stdout)["verdict"]
    return verdict


def getScanResult(scan_id):
    cmd = CMD_BASE + " scan_get_result " + scan_id
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    status = json.loads(stdout)
    status = status["scanners"]
    status = status[0]
    status = status["status"]
    return status


if __name__ == "__main__":
    # result = execute_analysis(function_name = "quick_scan_url", url = "https://efreidoc.fr/")
    # result = execute_analysis(function_name="quick_scan_url_file", url = "https://efreidoc.fr/L3/Chinois/CE/20XX-XX.CE.sujet.chin.pdf")

    result = execute_analysis(
        "quick_scan_file", filename="liste_classement_ecn_20210623_1042.pdf")
    print(result)
