

function CotizaUser($scope,$http,$filter,$location,$localStorage,NgMap) {

    $scope.riesgo = 8

    $scope.categoria = 1

    $scope.ubicL= true

    $scope.ubicP= true




  $scope.autoRotate = function() {
      if (vm.map.getTilt() != 0) {
        $interval(function() {
          var heading = vm.map.getHeading() || 0;
          vm.map.setHeading(heading + 90);
        }, 3000);
      }
    }
   

      


      function urlBase64Decode(str) {
        var output = str.replace('-', '+').replace('_', '/');
        switch (output.length % 4) {
            case 0:
                break;
            case 2:
                output += '==';
                break;
            case 3:
                output += '=';
                break;
            default:
                throw 'Illegal base64url string!';
        }
        return window.atob(output);
    }


    function getUserFromToken() {
        var token = $localStorage.token;
        var user = {};
        if (typeof token !== 'undefined') {
            var encoded = token.split('.')[1];
            user = JSON.parse(urlBase64Decode(encoded));
        }
        return user;
    }


    $scope.user = getUserFromToken().user_id

    








    $scope.antiguedad = [{
    id: 1,
    label: 'Nuevo',
   
    }, {
    id: 2,
    label: 'Usado',
  
    }];

    $scope.est_antiguedad = 'False'

    $scope.model = {}


    $scope.data = function (todo) {



    }

    // $scope.antig = function (todo) {

    //     console.log(todo)

    //     if($scope.model.modelo.id_modelo == undefined){


    //         console.log('ksksksk')
    //     }



    //     id_modelo = $scope.model.modelo.id_modelo



    //     if(todo.antiguedad.label == 'Usado'){

    //         $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

    //         console.log('precio',response)

           

    //         $http.get(host+"/preciodreprecio/"+response).success(function(response) {

    //         $scope.precio = response

    //         });

    //         });



          
    //     }

    //     if(todo.antiguedad.label == 'Nuevo'){

    //         //$scope.CurrentDate = new Date()

    //         //anio = $filter('date')($scope.CurrentDate, 'yyyy')

            
    //         $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

    //         console.log('precio',response)

    //         $scope.precio = response

    //         });






    //     }

    // }


    $scope.logear = function (todo) {


       
        $http({
        url: host+"/logearse/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {
          


        })

    }

    $http.get(host+"/estadologin/").success(function(response) {$scope.estadologin = response;

      
    });


    $http.get(host+"/marca/").success(function(response) {$scope.marca = response;

      
    });

    $http.get(host+"/uso/").success(function(response) {$scope.uso = response;

      
    });

    $http.get(host+"/anio/").success(function(response) {$scope.anio = response;


        //$scope.model.anio = $scope.anio[0]

      
    });


    $http.get(host+"/timon/").success(function(response) {$scope.timon = response;

      
    });

    $http.get(host+"/modalidad/").success(function(response) {$scope.modalidad = response;

        $scope.model.modalidad= $scope.modalidad[1]

      
    });

    //console.log($scope.items);




    $scope.obtenermodelo = function (data) {

       
    $http.get(host+"/modelo/"+data.marca.id_marca+'/').success(function(response) {

        $scope.modelo = response



      
    });

    }

    $scope.evaluaanio=function(data){


        if(data.id_anio<28){

            $scope.showantiguedad = false


        }
        else{

            $scope.showantiguedad = true
        }
    }


       
    $scope.obtenerclase = function (data) {
    
        $http.get(host+"/claseModelo/"+data.modelo.id_modelo+'/').success(function(response) {

            $scope.claseModelo = response



            $scope.vari= $scope.claseModelo[0].id

            $http.get(host+"/riesgomodelo/"+$scope.vari+'/').success(function(response) {


            varx = ''

            for (var i = 0; i < response.length; i++) {

                varx = varx +response[i].aseguradora__name_asegurad+'aseg'+response[i].id_riesg_id+'riesg'
            }

      


            $scope.riesgo = varx

            if (varx==''){

                $scope.riesgo = 3
            }



           
        });

       

      
    });





    }

    $scope.programa = 3

    $scope.ubicacion = 1


    $scope.obtenerprecio = function (data) {



  

        $http.get(host+"/precio/"+$scope.model.claseModelo.id_modelo+'/'+data.anio.anio_antig+'/').success(function(response) {


        $scope.precio = response
             
        });


    }


        $scope.obteneruso = function (data) {

        

  

        $http.get(host+"/usos/"+$scope.model.claseModelo.id_tipo).success(function(response) {


        $scope.uso = response
             
        });


    }



$scope.items = [{
id: 1,
label: 'Lima'
}, {
id: 2,
label: 'Provincia'
}];

$scope.selected = $scope.items[0];

$scope.saveContact = function (model,precio,check,ubicP,ubicL) {

        modelo = model.modelo.id_modelo

        tipo = model.claseModelo.id_tipo

        antiguedad = 'Usado'


        for (var prop in model) {

              if (prop == 'antiguedad'){

                antiguedad = model.antiguedad.label
                
              }
        
        }


        

        marca = model.marca.id_marca

        var todo={

            add: "Guardar",
            dato: model,
            precio:precio,
            ubicL:ubicL,
            ubicP:ubicP,
            check:check,
            modelo:modelo,
            done:false
        }



        if ($scope.check== 1){

            $scope.model.statuscheck = 1
        }
        else{
            $scope.model.statuscheck = 0

        }

        

        if ($scope.ubicL== 1){

            $scope.model.statusubicL = 1
        }
        else{
            $scope.model.statusubicL = 0

        }        


        if ($scope.ubicP== 1){

            $scope.model.statusubicP = 1
        }
        else{
            $scope.model.statusubicP = 0

        }  
        


        $http({
        url: host+"/cotiSave/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {



            console.log('Resultado...',data)

            $scope.id_cliente = data



      /// Trae Programas



        $http.get(host+"/asegprogram/"+4+"/"+model.modelo.id_modelo+'/'+model.uso+'/'+marca+'/'+tipo+'/'+$scope.precio+'/'+model.anio.id_anio).success(function(response) {


        $scope.pm = response; 

        if($scope.pm.length==0){

            $scope.pm=666

        }
        else{

            $scope.pm = $scope.pm[0].id_prog
        }



        $http.get(host+"/asegprogram/"+5+"/"+model.modelo.id_modelo+'/'+model.uso+'/'+marca+'/'+tipo+'/'+$scope.precio+'/'+model.anio.id_anio).success(function(response) {

                $scope.pr = response; 

                if($scope.pr.length==0){

                $scope.pr=666

                }
                else{

                $scope.pr = $scope.pr[0].id_prog

                }


                   $http.get(host+"/asegprogram/"+1+"/"+model.modelo.id_modelo+'/'+model.uso+'/'+marca+'/'+tipo+'/'+$scope.precio+'/'+model.anio.id_anio).success(function(response) {


                    $scope.pp = response; 

                    if($scope.pp.length==0){

                        $scope.pp=666

                    }
                    else{

                        $scope.pp= $scope.pp[0].id_prog
                    }

                programita = $scope.pm+'z'+$scope.pr+'z'+$scope.pp+'z9'


                                urlenvia = '/resultadouser/'+data+'/'+model.uso+'/'+model.anio.id_anio+'/'+model.modalidad.id_modalidad+'/'+programita+'/'+model.modelo.id_modelo+'/'+$scope.precio+'/'+tipo+'/'+marca+'/'+antiguedad

                todo = {

                    data:urlenvia
                }


                // Envia URL al backend
                
                        $http({
                        url: host+"/generapdf/",
                        data: todo,
                        method: 'POST',

                        }).
                        success(function(data) {


                            console.log('cliente....',$scope.id_cliente)


                            //Envia email

                                    todo = {

                                            data:$scope.id_cliente
                                    }

                                    $http({

                                        url: host+"/enviaemail",
                                        data: todo,
                                        method: 'POST',

                                    }).
                                    success(function(data) {

                                        console.log(data)


                                    })



                        })



                $location.url('/resultadouser/'+data+'/'+model.uso+'/'+model.anio.id_anio+'/'+model.modalidad.id_modalidad+'/'+programita+'/'+model.modelo.id_modelo+'/'+$scope.precio+'/'+tipo+'/'+marca+'/'+antiguedad)

                







               });


               });
        });

    })

    };


}

