'use strict';

var app = angular.module('mongoviz', []);
app.controller('VizController', 
	function($scope){
		$scope.fields = [];
		$scope.getFields = function(){
			$scope.fields = [
				{'Id': '1', 'Name': 'Teste'}
			];
		};
});