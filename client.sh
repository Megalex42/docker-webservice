echo "***************************************"
echo "TEST CLIENT - ADDING A FEW SAMPLE TASKS"
echo "***************************************"
#post some curl commands to the web service
#using webservice as alias from docker compose file
curl -d 'title=first task&description=do the laundry&start_date=2019/12/02&end_date=2019/12/1&priority=1&category=todo&status=started' webservice:8080/addTask
curl -d 'title=second task&description=buy some bread&start_date=2019/13/05&end_date=2019/10/2&priority=2&category=purchase&status=later' webservice:8080/addTask
curl -d 'title=third task&description=clean the car&start_date=2019/12/02&end_date=2019/12/1&priority=3&category=todo&status=soon' webservice:8080/addTask
curl -d 'title=fourth task&description=go to school&start_date=2019/11/08&end_date=2019/11/6&priority=4&category=activity&status=blah' webservice:8080/addTask
echo "***************************************"
echo "TEST CLIENT - GETTING TASKS FROM API"
echo "***************************************"
#get the tasks from webservice
#using webservice as alias from docker compose file
curl webservice:8080/getTasks
echo "***************************************"
echo "TEST CLIENT - END TESTS"
echo "***************************************"