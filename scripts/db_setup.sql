CREATE ROLE trafficuser WITH LOGIN PASSWORD 'trafficpassword';
GRANT ALL PRIVILEGES ON DATABASE traffic to trafficuser;
ALTER USER trafficuser CREATEDB;
CREATE EXTENSION postgis;
