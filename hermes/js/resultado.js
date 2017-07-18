
function Resultado($scope,$http,$filter,$routeParams,$location,$localStorage) {


$scope.items5 = [
{
  id: 0,
  label: '0%',
  value:'100'
},{
  id: 1,
  label: '1%',
  value:'99'
}, {
  id: 2,
  label: '2%',
  value:'98'
}, {
  id: 3,
  label: '3%',
  value:'97'
}, {
  id: 4,
  label: '4%',
  value:'96'
}, {
  id: 5,
  label: '5%',
  value:'95'
}];


$scope.items8 = [
{
  id: 0,
  label: '0%',
  value:'100'
},{
  id: 1,
  label: '1%',
  value:'99'
}, {
  id: 2,
  label: '2%',
  value:'98'
}, {
  id: 3,
  label: '3%',
  value:'97'
}, {
  id: 4,
  label: '4%',
  value:'96'
}, {
  id: 5,
  label: '5%',
  value:'95'
}, {
  id: 5,
  label: '6%',
  value:'94'
},
 {
  id: 5,
  label: '7%',
  value:'93'
},
{
  id: 5,
  label: '8%',
  value:'92'
}
];



    $scope.descuento = function(descuento){





         $scope.traeprima(descuento.value)
    }


    $scope.calculo = function (data) {


            var todo = {
                monto:$routeParams,
                data:data
            }


            $http({
            url: host+"/tasaadmin/",
            data: todo,
            method: 'POST',
         
            }).
            success(function(data) {



                    
                $scope.model.tasahdi = data[0]['tasahdi']
                $scope.model.tasapositiva = data[3]['tasapositiva']
                $scope.model.tasamapfre = data[1]['tasamapfre']
                $scope.model.tasapacifico = data[2]['tasapacifico']
                $scope.model.tasarimac = data[4]['tasarimac']

                $scope.hdi = data[0]['hdi']
                $scope.positiva = data[3]['positiva']
                $scope.mapfre = data[1]['mapfre']
                $scope.pacifico = data[2]['pacifico']
                $scope.rimac = 77777777

                $scope.phdisubtotal = data[0]['phdisubtotal']
                $scope.positivasubtotal = data[3]['positivasubtotal']
                $scope.mapfresubtotal = data[1]['mapfresubtotal']
                $scope.pacificosubtotal = data[2]['pacificosubtotal']
                $scope.rimacsubtotal = data[4]['rimacsubtotal']

                $scope.phditotal = data[0]['phditotal']
                $scope.positivatotal = data[3]['positivatotal']
                $scope.mapfretotal = data[1]['mapfretotal']
                $scope.pacificototal = data[2]['pacificototal']
                $scope.rimactotal = data[4]['rimactotal']

                /*Pdf Genera*/

                // $scope.pdf = {}



                // $scope.pdf.tasahdi = data[0]['tasahdi']
                // $scope.pdf.tasapositiva = data[3]['tasapositiva']
                // $scope.pdf.tasamapfre = data[1]['tasamapfre']
                // $scope.pdf.tasapacifico = data[2]['tasapacifico']
                // $scope.pdf.tasarimac = data[4]['tasarimac']

                // $scope.pdf.hdi = data[0]['hdi']
                // $scope.pdf.positiva = data[3]['positiva']
                // $scope.pdf.mapfre = data[1]['mapfre']
                // $scope.pdf.pacifico = data[2]['pacifico']
                // $scope.pdf.rimac = data[4]['rimac']

                // $scope.pdf.phdisubtotal = data[0]['phdisubtotal']
                // $scope.pdf.positivasubtotal = data[3]['positivasubtotal']
                // $scope.pdf.mapfresubtotal = data[1]['mapfresubtotal']
                // $scope.pdf.pacificosubtotal = data[2]['pacificosubtotal']
                // $scope.pdf.rimacsubtotal = data[4]['rimacsubtotal']

                // $scope.pdf.phditotal = data[0]['phditotal']
                // $scope.pdf.positivatotal = data[3]['positivatotal']
                // $scope.pdf.mapfretotal = data[1]['mapfretotal']
                // $scope.pdf.pacificototal = data[2]['pacificototal']
                // $scope.pdf.rimactotal = data[4]['rimactotal']

                // $scope.riesgorimac = data[4]['riesgorimac']

                // $http({

                //     url: host+"/recibetasas/",
                //     data: $scope.pdf,
                //     method: 'POST',

                //     })

            })


    }

    if($localStorage.token){ 

	    $http.get(host+"/perfil/").success(function(response) {

            console.log('perfil',response)

            $scope.perfil = response

            });
    }


    $scope.order_id = $routeParams.orderId;


    $scope.uso = $routeParams.uso

    $scope.tipo = $routeParams.tipo

    $scope.modalidad = $routeParams.modalidad

    $scope.anio = $routeParams.anio

    $scope.monto = $routeParams.precio



    $scope.marca = $routeParams.marca


    $scope.riesgo = $routeParams.riesgo

    $scope.categoria = $routeParams.categoria

    $scope.ubicacion = $routeParams.ubicacion

    $scope.categoria = $routeParams.categoria

    $scope.modelo = $routeParams.modelo

    $scope.parametros = $routeParams

    $scope.absUrl = $location.absUrl();


    

    if($scope.parametros.programa.split('z')[1]!='2' || $scope.parametros.programa.split('z')[1]!='25' || $scope.parametros.programa.split('z')[1]!='26'){

        $scope.muestradescuento=false

    }



    $scope.model = {}
    $scope.datamodel = {}

    $http.get(host+"/programas/").success(function(response) {$scope.programas = response;

    $scope.model.programa = $scope.programas[3]

    //$scope.programa($scope.model)


    });





  $http.get(host+"/getgps/"+$scope.modelo+"/"+$scope.marca+"/"+$scope.tipo+"/"+$scope.uso+"/"+$scope.monto+'/'+$scope.anio+'/'+$scope.parametros.programa).success(function(response) {

      $http({
        
        url: host+"/recibegps/",
        data: response,
        method: 'POST',
     
        })

    $scope.gps = response

  });



    $http.get(host+"/datosfiltro/"+$scope.order_id+"/").success(function(response) {$scope.cliente = response[0];

        var f = new Date();

          $http({

            url: host+"/recibecliente/",
            data: response,
            method: 'POST',
         
            })


        $scope.cliente.fecha = f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear()

    });

    $scope.programapositiva = function (data) {


        $scope.positiv = data.programam.id_prog 

        $scope.p = $scope.parametros.programa.split('z')

        $scope.programa= $scope.p[0]+'z'+$scope.positiv+'z'+$scope.p[2]+'z9'

        $scope.parametros.programa = $scope.programa

        $scope.traeprima(100)

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            // $http({
            // url: host+"/recibecoberturas/",
            // data: $scope.cobertura,
            // method: 'POST',
         
            // })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.deducible = response;

            //   $http({
            // url: host+"/recibededucibles/",
            // data: $scope.deducible,
            // method: 'POST',
         
            // })

        });

    }

    $scope.programamapfre = function (data) {


        $scope.mafe = data.programam.id_prog 

        $scope.p = $scope.parametros.programa.split('z')

        $scope.programa= $scope.p[0]+'z'+$scope.mafe+'z'+$scope.p[2]+'z9'

        $scope.parametros.programa = $scope.programa

        $scope.traeprima(100)

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            // $http({
            // url: host+"/recibecoberturas/",
            // data: $scope.cobertura,
            // method: 'POST',
         
            // })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.deducible = response;

            //   $http({
            // url: host+"/recibededucibles/",
            // data: $scope.deducible,
            // method: 'POST',
         
            // })

        });

    }



    $scope.programarimac = function (data) {

    $scope.muestradescuento = false

    $scope.ri = data.programar.id_prog

        $scope.p = $scope.parametros.programa.split('z')

        $scope.programa= $scope.p[0]+'z'+$scope.ri+'z'+$scope.p[2]+'z9'

        $scope.parametros.programa = $scope.programa

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            // $http({
            // url: host+"/recibecoberturas/",
            // data: $scope.cobertura,
            // method: 'POST',
         
            // })

        });


        $scope.traeprima(100)

        if ($scope.ri=='2' || $scope.ri=='25' || $scope.ri=='26'){

            $scope.muestradescuento = true
        }

        $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

          // $http({
          //   url: host+"/recibededucibles/",
          //   data: $scope.deducible,
          //   method: 'POST',
         
          //   })

        });

    }

    // $scope.programapositiva = function (data) {

      

    //     $scope.posi = data.programap.id_prog

    //     console.log($scope.posi)

    //     $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

    //     $scope.parametros.programa = $scope.programa

    //     console.log('programa',$scope.programa)

    //     $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

    //         $scope.cobertura = response;

    //         $http({
    //         url: host+"/recibecoberturas/",
    //         data: $scope.cobertura,
    //         method: 'POST',
         
    //         })

    //     });

    //      $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

    //     $scope.deducible = response;

    //       $http({
    //         url: host+"/recibededucibles/",
    //         data: $scope.deducible,
    //         method: 'POST',
         
    //         })

    //     });

    // }

    // $scope.programapacifico = function (data) {

    //     $scope.pa = data.programapa.id_prog


    //     console.log($scope.pa)


    //     console.log($scope.parametros.programa)


      

    //     console.log('programa',$scope.programa)

    //     $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

    //         $scope.cobertura = response;

    //         $http({
    //         url: host+"/recibecoberturas/",
    //         data: $scope.cobertura,
    //         method: 'POST',
         
    //         })

    //     });

    //      $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

    //     $scope.deducible = response;

    //       $http({
    //         url: host+"/recibededucibles/",
    //         data: $scope.deducible,
    //         method: 'POST',
         
    //         })

    //     });

    // }



    $scope.uploadpdf = function () {


            $http({
            url: host+"/pdfx/",
            data: $scope.absUrl,
            method: 'POST',
         
            }).
            success(function(data) {

             window.open('http://cotizador.hermes.pe:8000/pdfout', "_blank");

            })


    }




        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.parametros.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            console.log('$scope.cobertura',$scope.cobertura)

            // $http({
            // url: host+"/recibecoberturas/",
            // data: $scope.cobertura,
            // method: 'POST',
         
            // })

            // $http({
            // url: host+"/pdfx/",
            // data: $scope.absUrl,
            // method: 'POST',
         
            // }).
            // success(function(data) {
            // })

        });




        $http.get(host+"/servic/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.parametros.programa+"/").success(function(response) {

        $scope.servic = response;

        console.log('servic HDI',$scope.servic)

        // $http({
        //     url: host+"/recibeservicios/",
        //     data: $scope.servic,
        //     method: 'POST',
         
        //     })

        });

        /*
        $http.get(host+"/financ/").success(function(response) {

        $scope.financ = response;


        });

*/


     $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.parametros.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

        console.log('deducible...',$scope.deducible)

          // $http({
          //   url: host+"/recibededucibles/",
          //   data: $scope.deducible,
          //   method: 'POST',
         
          //   })

        });


    $scope.model = {}

    $scope.traeprima = function(descuento){

    console.log('enviando parametros',$scope.parametros)

    $http({

        url: host+"/primaneta/"+descuento,
        data: $scope.parametros,
        method: 'POST',

    }).
    success(function(data) {

        console.log('Prima Neta',data)

        $scope.model.tasahdi = data[0]['tasahdi']
        $scope.model.tasapositiva = data[3]['tasapositiva']
        $scope.model.tasamapfre = data[1]['tasamapfre']
        $scope.model.tasapacifico = data[2]['tasapacifico']
        $scope.model.tasarimac = data[4]['tasarimac']

        $scope.hdi = data[0]['hdi']
        $scope.positiva = data[3]['positiva']
        $scope.mapfre = data[1]['mapfre']
        $scope.pacifico = data[2]['pacifico']
        $scope.rimac = data[4]['rimac']

        $scope.hdisubtotal = data[0]['hdisubtotal']
        $scope.positivasubtotal = data[3]['positivasubtotal']
        $scope.mapfresubtotal = data[1]['mapfresubtotal']
        $scope.pacificosubtotal = data[2]['pacificosubtotal']
        $scope.rimacsubtotal = data[4]['rimacsubtotal']

        $scope.hditotal = data[0]['hditotal']
        $scope.positivatotal = data[3]['positivatotal']
        $scope.mapfretotal = data[1]['mapfretotal']
        $scope.pacificototal = data[2]['pacificototal']
        $scope.rimactotal = data[4]['rimactotal']

        $scope.riesgomapfre =data[1]['riesgomapfre']
        $scope.idriesgomapfre =data[1]['idriesgomapfre'] 

        $scope.riesgohdi =data[0]['riesgohdi']
        $scope.idriesgohdi =data[0]['idriesgohdi']      

        $scope.riesgorimac =data[4]['riesgo']
        $scope.idriesgo =data[4]['idriesgo']


        $scope.riesgopositiva =data[3]['riesgopositiva']
        $scope.idriesgopositiva =data[3]['idriesgopositiva']

        $scope.riesgopacifico =data[2]['riesgopacifico']
        $scope.idriesgopacifico =data[2]['idriesgopacifico']

        if($scope.idriesgo == 5 || $scope.idriesgo==6){

            $scope.items = $scope.items5
        }
         if($scope.idriesgo == 4 || $scope.idriesgo==7){

            $scope.items = $scope.items8
        }



        /// Trae Financiamiento


        $routeParams.hditotal =$scope.hditotal
        $routeParams.positivatotal  =$scope.positivatotal
        $routeParams.mapfretotal =$scope.mapfretotal
        $routeParams.pacificototal  =$scope.pacificototal
        $routeParams.rimactotal=$scope.rimactotal

        console.log('nuevas primas')


            $http({

            url: host+"/fiiiii/",
            data: $routeParams,
            method: 'POST',

            }).
            success(function(data) {

            console.log('yape............',data)

            $scope.financ = data


            })




                /*Pdf Genera*/

        // $scope.pdf = {}



        // $scope.pdf.tasahdi = data[0]['tasahdi']
        // $scope.pdf.tasapositiva = data[3]['tasapositiva']
        // $scope.pdf.tasamapfre = data[1]['tasamapfre']
        // $scope.pdf.tasapacifico = data[2]['tasapacifico']
        // $scope.pdf.tasarimac = data[4]['tasarimac']

        // $scope.pdf.hdi = data[0]['hdi']
        // $scope.pdf.positiva = data[3]['positiva']
        // $scope.pdf.mapfre = data[1]['mapfre']
        // $scope.pdf.pacifico = data[2]['pacifico']
        // $scope.pdf.rimac = data[4]['rimac']

        // $scope.pdf.phdisubtotal = data[0]['phdisubtotal']
        // $scope.pdf.positivasubtotal = data[3]['positivasubtotal']
        // $scope.pdf.mapfresubtotal = data[1]['mapfresubtotal']
        // $scope.pdf.pacificosubtotal = data[2]['pacificosubtotal']
        // $scope.pdf.rimacsubtotal = data[4]['rimacsubtotal']

        // $scope.pdf.phditotal = data[0]['phditotal']
        // $scope.pdf.positivatotal = data[3]['positivatotal']
        // $scope.pdf.mapfretotal = data[1]['mapfretotal']
        // $scope.pdf.pacificototal = data[2]['pacificototal']
        // $scope.pdf.rimactotal = data[4]['rimactotal']

        // $http({

        //     url: host+"/recibetasas/",
        //     data: $scope.pdf,
        //     method: 'POST',

        //     })

    })


    }

    $scope.traeprima(100)



  /// Trae Programas 

  $http.get(host+"/asegprogram/"+1+"/"+$scope.modelo+'/'+$scope.uso+'/'+$scope.marca+'/'+$scope.tipo+'/'+$scope.monto).success(function(response) {$scope.programaspositiva = response; $scope.model.programap = $scope.programaspositiva[0]});
  $http.get(host+"/asegprogram/"+2+"/"+$scope.modelo+'/'+$scope.uso+'/'+$scope.marca+'/'+$scope.tipo+'/'+$scope.monto).success(function(response) {$scope.programaspacifico = response;});
  $http.get(host+"/asegprogram/"+3+"/"+$scope.modelo+'/'+$scope.uso+'/'+$scope.marca+'/'+$scope.tipo+'/'+$scope.monto).success(function(response) {$scope.programashdi = response;});
  $http.get(host+"/asegprogram/"+4+"/"+$scope.modelo+'/'+$scope.uso+'/'+$scope.marca+'/'+$scope.tipo+'/'+$scope.monto).success(function(response) {$scope.programasmapfre = response; $scope.model.programam = $scope.programasmapfre[0]});
  $http.get(host+"/asegprogram/"+5+"/"+$scope.modelo+'/'+$scope.uso+'/'+$scope.marca+'/'+$scope.tipo+'/'+$scope.monto).success(function(response) {$scope.programasrimac = response; $scope.model.programar = $scope.programasrimac[0]});

       




    // $http({

    //     url: host+"/enviaemail/",
    //     data: $routeParams,
    //     method: 'POST',

    // }).
    // success(function(data) {

    //     console.log(data)


    // })









}

