var buddyuppoc = angular.module('buddyuppoc', ['ngRoute', 'firebase']);

buddyuppoc.config(function($routeProvider, $sceDelegateProvider) {
    $routeProvider

        // route for the poc page
        .when('/', {
            templateUrl : window.STATIC_URL + 'main_site/js/pages/poc.html',
            controller  : 'mainController'
        })
        .when('/stats', {
            templateUrl : window.STATIC_URL + 'main_site/js/pages/stats.html',
            controller  : 'statsController'
        })
        // // route for another page
        // .when('/another', {
        //     templateUrl : 'pages/another.html',
        //     controller  : 'anotherController'
        // })

     $sceDelegateProvider.resourceUrlWhitelist([
        // Allow same origin resource loads.
        'self',
        // Allow loading from our assets domain.  Notice the difference between * and **.
        window.STATIC_URL + '**'
    ]);
});

buddyuppoc.controller('mainController', ['$scope', '$firebase', '$http', function($scope, $firebase, $http) {
    $scope.init_poc = function() {
        var ref = new Firebase("https://glowing-torch-3186.firebaseio.com/messages");
        ref.orderByChild("timestamp");
        $scope.sync = $firebase(ref);
        var syncObject = $scope.sync.$asObject();
            // synchronize the object with a three-way data binding
            // click on `index.html` above to see it used in the DOM!
        syncObject.$bindTo($scope, "data");
        // $scope.messages = sync.$asArray();
        $scope.uuid = Date.now();
        angular.element('input[name=new_message]').trigger('focus');
    }
    
    $scope.submit_message = function() {
        console.log("submit: "+$scope.new_message);
        // $http
        message = {
            "body": $scope.new_message,
            "uuid": $scope.uuid
        }
        console.log($scope.sync)
        $scope.sync.$push(message)
        $http.post("/chat_posted", message);
        $scope.new_message = "";
    }
}]);
buddyuppoc.controller('statsController', ['$scope', '$firebase', '$http', function($scope, $firebase, $http) {
    $scope.init_stats = function() {
        var ref = new Firebase("https://glowing-torch-3186.firebaseio.com/status/");
        var sync = $firebase(ref);
        var syncObject = sync.$asObject();
        syncObject.$bindTo($scope, "data");
    }

}]);