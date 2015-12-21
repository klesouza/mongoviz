'use strict';

var app = angular.module('mongoviz', []);
app.controller('VizController',
function($scope, $http){
	$scope.fields = [];
	$scope.aggs = ["count", "sum"];
	$scope.model = {
		server: "localhost",
		port: "27017",
		db: "test",
		collection: ""
	};
	$scope.queryModel = {
		selectedField: '',
		selectedAgg: '',
		selectedAggField: '',
		selectedFilter: ''
	};
	$scope.showAggField = false;
	function buildURL(){
		return '/'+$scope.model.server+'/'+$scope.model.port+'/'+$scope.model.db+'/'+$scope.model.collection;
	};
	$scope.selectField = function(target, sel, fn){
		$scope.queryModel[target] = sel;
		if(fn)
		fn(sel)
	};
	$scope.getFields = function(){
		$http({
			method: 'GET',
			url: buildURL()
		}).then(function success(response){
			$scope.fields = response.data.fields;
		},
		function error(response){
			$scope.fields = [];
		});
	};
	$scope.toggleAggField = function (sel) {
		$scope.showAggField = sel == 'sum';
	}

	$scope.plot = function(){
		$http({
			method: 'GET',
			url: buildURL()+'/plot',
			data: {}
		}).then(function success(response){
			chart(response.data);
		}, function error(response) {
		});
	};

	function chart(data){
		$("#chart").highcharts(data);
	};
});
