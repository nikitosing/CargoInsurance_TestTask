# CargoInsurance_TestTask
##How to start
###1. Clone repo:
	```git clone https://github.com/nikitosing/CargoInsurance_TestTask.git```
###2. Change directory:
	```cd CargoInsurance_TestTask```
###3. Build docker 
	```docker build -t test_task ./```
###4. Run docker
	```docker run -d --name test_ran -p 80:80 test_task```
###5. Go to http://127.0.0.1:80/docs/