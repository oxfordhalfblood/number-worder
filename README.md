1. make workspace folder
2. Open terminal
3. change directory by using:
    `cd /your_path/number-worder`
4. chmod +x mainapp.exe
5. Execute the app by using (You can use any number you want instead of 23):
    ./mainapp.exe 23  
6. links: https://stackoverflow.com/questions/10516201/updating-and-committing-only-a-files-permissions-using-git-version-control
7. https://stackoverflow.com/questions/21691202/how-to-create-file-execute-mode-permissions-in-git-on-windows
8. Docker:
`docker build -t python-barcode .`
`docker run --rm python-barcode 20`
9. 
pip install pipenv
pipenv run python converterTest.py
pipenv run python ./mainapp.exe 32


10. For git steps:
    git add .
    git commit -m "Initial commit"
    <create a github repo without readme.>
    git remote add origin https://github.com/oxfordhalfblood/number-worder.git
    git push -u origin master

11. CI links: https://circleci.com/blog/setting-up-continuous-integration-with-github/



