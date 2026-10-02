function totalPrice(items) {
    let total = 0;
    for (let i = 0; i <= items.length; i++) {
        total += items[i].price;
    }
    return total;
}

const cart = [
    { price: "10" },
    { price: 20 },
    { price: 5 },
];

const result = totalPrice(cart);
console.log("Cart total:", result);
