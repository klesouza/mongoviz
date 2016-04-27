# mongoviz
A simple project for visualizing mongoDB aggregation operations.
It's a project with study purposes, I've used Python/Flask, some angularJS and MongoDB.

# Example  
> {$group: {"_id": "&grouping_field", "y": {"$sum": 1}}}
> {$group: {"_id": {"group1": "$grouping_field1", "group2": "$grouping_field2"}, "y": {"$sum": 1}}},  
> {$group: {"_id": "$_id.group1", "series": {"$addToSet": {"name": "$_id.group2", "y": "$y"}}}}

# Docker
> $ docker-compose -f dockerfiles/docker-compose.yml -p mongoviz up -d   
> $ docker exec -it [mongo-container-id] seed  

On your browser http://[docker-ip]:5000/test/example  
![access](/images/access.png)
Load one of the pipelines located on the /examples folder
![access](/images/access1.png)
Data source: [FNS Estado Gestão do SUS](http://api.pgi.gov.br/api/1/serie/2440.json)
