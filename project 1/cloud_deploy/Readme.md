In this repo, the same predictive model is deployed to AWS. 

The first step is to install the awsebcli:

```console
pipenv install awsebcli --dev
```

![awsebcli install](screenshots\awsebcli_install.jpg)

Then we can test it locally before deploying it to the clouds:

![local test](screenshots\eb_local_deploy.jpg)


Now we can create an application with:

```console
eb create leaveornot-env
```

With the predict_test.py file we can test the deployment:

![deployment test](screenshots\cloud_deploy_test.jpg)

THe application can be tracked via the aws dashboard as well:

![dashboard](screenshots\aws_dashboard.jpg)