    var module = angular.module("App", ['ngRoute','elif','ngStorage','ngMap']);

  

    host ='http://cotizador.hermes.pe:8000'


    module.config(['$routeProvider','$httpProvider',

        function($routeProvider,$httpProvider) {

            $routeProvider.

                when('/cotiza', {
                    templateUrl: 'webcotiz.html',
                    controller: 'Cotiza'
                }).
                when('/resultado/:orderId/:uso/:anio/:modalidad/:programa/:modelo/:precio/:tipo/:marca', {
                    templateUrl: 'resultadofiltro.html',
                    controller: 'Resultado'

                }).

                when('/upload', {
                    templateUrl: 'upload.html',
                    controller: 'Admin'
                }).

                when('/admin', {
                    templateUrl: 'admin.html',
                    controller: 'Admin'
                }).
                 when('/deducibles', {
                    templateUrl: 'deducible.html',
                    controller: 'Admin'
                }).

                 when('/servicios', {
                    templateUrl: 'servicios.html',
                    controller: 'Admin'
                }).
                when('/tasas', {
                    templateUrl: 'tasas.html',
                    controller: 'Admin'
                }).
                when('/autos', {
                    templateUrl: 'autos.html',
                    controller: 'Admin'
                }).
                when('/parametros', {
                    templateUrl: 'parametros.html',
                    controller: 'Admin'
                }).
                
                when('/riesgos', {
                    templateUrl: 'riesgos.html',
                    controller: 'Admin'
                }).

                when('/financiamiento', {
                    templateUrl: 'financiamiento.html',
                    controller: 'Admin'
                }).
                when('/primas', {
                    templateUrl: 'primas.html',
                    controller: 'Admin'
                }).
                 when('/politicas', {
                    templateUrl: 'politicas.html',
                    controller: 'Admin'
                }).


                otherwise({
                    redirectTo: '/cotiza'
                });

        $httpProvider.interceptors.push(['$q', '$location', '$localStorage', function($q, $location, $localStorage) {
        return {
                'request': function (config) {
                    config.headers = config.headers || {};
                    if ($localStorage.token) {
                        config.headers.Authorization = 'Bearer ' + $localStorage.token;
                    }
                    return config;
                },
                'responseError': function(response) {
                    if(response.status === 401 || response.status === 403) {
                        $location.path('/signin');
                    }
                    return $q.reject(response);
                }
            };
        }]);

        }]);

//uso,tipo,modalidad,anio,programa 8 6 2 2008 1

