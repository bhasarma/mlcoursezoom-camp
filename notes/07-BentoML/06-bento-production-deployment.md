## 7.6 Bento production Deployment

In this module, we are going to:

- build a bento out of the service that we have been using, 
- create a docker container  out of it and 
- deploy that container into AWS in their service called ECS (Elastic Container Service). 

Google as well as Azure has very similar services for deploying containers. It's a very scalable way of getting our service running and scaling up preetty high. It is a nice default way to get our service out there. If we have different types of scaling properties that are more nuanced, there are other ways that we can deploy, but this is a fairly scalable way out of the box. 

We start with `service.py`. We insert the model that has batching enabled. We have async and await. Then we build the bento with:

```bash
(bentoml) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK07-BentoML-production-ready-ML/7-6-bento-production-deployment$ bentoml build
Building BentoML service "credit_risk_classifier:spbfbycupoqd6k47" from build context "/home/bsarma/GitHub/mlcoursezoom-camp/WK07-BentoML-production-ready-ML/7-6-bento-production-deployment"
Packing model "credit_risk_model:hziru3culorhtyyh"
Locking PyPI package versions..

██████╗░███████╗███╗░░██╗████████╗░█████╗░███╗░░░███╗██╗░░░░░
██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗████╗░████║██║░░░░░
██████╦╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██╔████╔██║██║░░░░░
██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██║░░██║██║╚██╔╝██║██║░░░░░
██████╦╝███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░╚═╝░██║███████╗
╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

Successfully built Bento(tag="credit_risk_classifier:spbfbycupoqd6k47")
```

Here our model `"credit_risk_model:hziru3culorhtyyh"` is built and we get the bento `"credit_risk_classifier:spbfbycupoqd6k47"`. We'll take this bento and then we'll containerize it with:

```bash
bentoml containerize credit_risk_classifier:spbfbycupoqd6k47
```
So, we have just built our bento container. We can run it now with `docker run` command.