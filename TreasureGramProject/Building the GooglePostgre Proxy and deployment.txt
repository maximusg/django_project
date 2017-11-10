Hooking up Django to GCLOUD

1) Go to: https://cloud.google.com/python/django/flexible-environment
2)Follow steps undtil step for "initialize your Cloud SQL Instance". Must first set up a service account
	A) Service account setup follow step 3: https://cloud.google.com/sql/docs/mysql/sql-proxy#keeping_the_proxy_up_to_date
3)Continue on to step 4 to start Proxy using Service account Credential made in 2.A
4)Command to run for me Specfically now is: .\cloud_sql_proxy.exe -instances="maxtestermaster:us-central1:maxtestermastersql"=tcp:5432 -credential_file='.\SQLCERT\privateProxyUser\maxtestermaster-1ec7a81318e0.json'
