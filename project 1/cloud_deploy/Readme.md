In this repo, the same predictive model is deployed to AWS. 

The first step is to install the awsebcli:

```console
pipenv install awsebcli --dev
```

![awsebcli install](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/cloud_deploy/screenshots/awsebcli_install.jpg)

Then we can test it locally before deploying it to the clouds:

![local test](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/cloud_deploy/screenshots/eb_local_deploy.jpg)


Now we can create an application with:

```console
eb create leaveornot-env
```

With the predict_test.py file we can test the deployment:

![deployment test](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/cloud_deploy/screenshots/cloud_deploy_test.jpg)

THe application can be tracked via the aws dashboard as well:

![dashboard](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/cloud_deploy/screenshots/aws_dashboard.jpg)
