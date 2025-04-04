import fnmatch
import re
import time
from invoke import Context, task
import zipfile
import os
from glob import glob

version = '0.7.1'
vol_files = {"volume": ["jserv-main.db", "doc-jserv.db"]}

@task
def create_volume(c):
    for vol, fs in vol_files.items():
        if not os.path.isdir(vol):
            os.mkdir(vol)
        for fn in fs: 
            with open(os.path.join(vol, fn), 'a') as vf:
                print(f'Volume file created: {os.path.join(vol, fn)}')
                vf.close()

# def post_check(config: dict):
#     warns = []
#     # web-dist/report.html
#     report = os.path.join(config.webdist, "report.html")
#     if not os.path.isfile(report):
#         raise FileNotFoundError(report)

#     ft = os.path.getctime(report)
#     if (time.time() - ft) > 600:
#         warns.append(f'{config.webdist}/report.html is created more than 10 minutes ago.')
    
#     return warns
        
@task
def build(c):
    buildcmds = {
        'webpack': '../../../anclient/examples/example.js/album',
        'mvn clean compile package -DskipTests': '../../../semantic-jserv/jserv-album',
    }
    err = False
    for cmd, pth in buildcmds.items():
        print(pth, cmd)
        ret = c.run(f'cd {pth} && {cmd}')
        print('OK:', ret.ok, ret.stderr)
    return err


@task(create_volume, build)
def make(c, zip=f'jserv-portfolio-{version}.zip'):
    """
    Create a ZIP file (jserv.zip).
    
    Args:
        c: Invoke Context object for running commands.
        zip: Name of the output ZIP file (default: "jserv-album.zip").
    """
    resources = {
        "bin/jserv-album-0.7.1.jar": ".",
        "bin/exiftool.exe": ".",
        "portfolio-synode-0.7-py3-none-any.whl": ".",
        "WEB-INF": "web-inf/*",
        "winsrv": "winsrv/*",
        "web-dist": "web-dist/*"  # This will match all files in web-dist/
    }

    excludes = ["*.logs", "report.html"];


    def matches_patterns(filename, patterns):
        """
        Check if a filename matches any of the given patterns.
        
        Args:
            filename (str): The filename to check (e.g., "data.logs").
            patterns (list): List of patterns (e.g., ["*.logs", "*.dat"]).
        
        Returns:
            bool: True if the filename matches any pattern, False otherwise.
        """
        return any(fnmatch.fnmatch(os.path.basename(filename), pattern) for pattern in patterns)

    try:
        err = False

        # err = build(c, buildcmds)

        # Ensure the output directory for the ZIP exists
        output_dir = os.path.dirname(zip) or "."
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        if os.path.isfile(zip):
            os.remove(zip)

        with zipfile.ZipFile(zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # resources
            for rk, rv in resources.items():
                if "*" in rv:  # Handle wildcard (e.g., web-dist/*)
                    # Use glob to expand wildcards in Python
                    count = 0
                    srcroot = re.sub('\\*$', '', rv.replace('\\', '/'))
                    for pth, _dir, fs in os.walk(srcroot):
                        for file in fs:
                            # if file and os.path.exists(file) and not matches_patterns(file, excludes):
                            if not matches_patterns(file, excludes):
                                file_path = os.path.join(pth, file)
                                relative_path = os.path.relpath(file_path, srcroot)
                                arcname = os.path.join(rk, relative_path)
                                zipf.write(file_path, arcname)
                                count += 1
                                print(f"Added to ZIP: {file_path} as {arcname}")
                    if count == 0:
                        err = True
                        print(f'No files found in {rv}.')
                else:  # Handle single files (jserv.jar and exiftool.exe)
                    file = rk if rv == '.' else rk
                    if os.path.exists(file):
                        zipf.write(file, rk)
                        print(f"Added to ZIP: {file} as {rk}")
                    else:
                        err = True
                        print(f"Warning: Resource '{file}' not found, skipping.")

            for rk, files in vol_files.items():
                for file in files:
                    file = os.path.join(rk, file)
                    if os.path.exists(file):
                        zipf.write(file, file)
                        print(f"Added volume file to ZIP: {file} as {rk}")
                    else:
                        err = True
                        print(f"Warning: volume file '{file}' not found, skipping.")


        print(f"Created ZIP file{' successfully' if not err else ' with errors'}: {zip}")

    except Exception as e:
        print(f"Error creating ZIP file: {str(e)}")
        raise

if __name__ == '__main__':
    from invoke import Program
    Program(namespace=globals()).run()
