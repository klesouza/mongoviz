# mongoviz
A simple project for visualizing mongoDB aggregation operations.
It's a project with study purposes, I've used Python/Flask, some angularJS and MongoDB.

### Example 
###### Simplest  
```
{$group: {"_id": "$grouping_field", "y": {"$sum": 1}}}  
```
###### Using Series
```
{$group: {"_id": {"group1": "$grouping_field1", "group2": "$grouping_field2"}, "y": {"$sum": 1}}},  
{$group: {"_id": "$_id.group1", "series": {$addToSet: {"name": "$_id.group2", "y": "$y"}}}}
```
