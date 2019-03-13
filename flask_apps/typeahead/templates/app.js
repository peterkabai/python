var app = angular.module('selectDemo', ['ngResource', 'oi.select']);

app.factory('ShopArr', function ($resource) {
    return $resource('shopArr.json', {}, {
        query: {method: 'GET', cache: true, isArray: true}
		//local: ["roo","loo","boo","moo","too"]
      }
    );
  })

app.controller('MainCtrl', function($scope, ShopArr, oiSelect) {
  $scope.version = oiSelect.version.full;
  
  $scope.shopArr = ShopArr.query();
  
  $scope.bundle = [];
});
