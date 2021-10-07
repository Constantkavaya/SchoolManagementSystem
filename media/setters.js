const kiosk={
     Fruit:"passion",
    get getFruit(){
        return this.Fruit;
    },
    set setsFruit(newFruits){
       this.Fruit="newFruits"
        
    
    }
};
console.log (kiosk.Fruit);
kiosk.newFruits="blueberries,Avocado";
console.log (kiosk.newFruits)
    