from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "postgresql://zwqyodsovxkzbg:fac4cc02ab1f949085f1b75f2cf313fbddfc92a8858bb8668474152f86b03583@ec2-35-168-122-84.compute-1.amazonaws.com:5432/de7mgrp7ccussv"
SECRET_KEY = "secret key"
JWT_EXPIRATION_DELTA = timedelta(minutes=30)
ENV = "DEVELOPMENT"
