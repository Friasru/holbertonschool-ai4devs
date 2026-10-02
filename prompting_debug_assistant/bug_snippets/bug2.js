function totalPrice(items) {
    let total = 0;
    for (let i = 0; i <= items.length; i++) {
        total += items[i].price;
    }
}

const cart = [{ price: "10" }, { price: 20 }, { price: 5 }];
console.log(totalPrice(cart));
