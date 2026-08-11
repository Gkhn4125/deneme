/* ?Veri türleri ve değişkenler
    ----- ilkel veri türleri -----
    1- number : sayısal veri türüdür. Örnek: 10, 3.14, -5
    2- string : metin veri türüdür. Örnek: "Merhaba", 'Dünya', `JavaScript`
    3- boolean : mantıksal veri türüdür. Örnek: true, false
    4- null : boş değer veri türüdür. Örnek: null
    5- undefined : tanımsız değer veri türüdür. Örnek: undefined
    6- bigint : büyük tam sayı veri türüdür. Örnek: 9007199254740991n
    7- symbol : benzersiz ve değiştirilemez bir veri türüdür. Örnek: Symbol('a')
    ----- referans veri türleri -----
    8- object : nesne veri türüdür. Örnek: {isim: "Ali", yaş: 25}
    9- function : fonksiyon veri türüdür. Örnek: function topla(a, b) { return a + b; }
    10- array : dizi veri türüdür. Örnek: [1, 2, 3, 4, 5]
    ----- değişken tanımlama -----
    11- var, let, const

    ilkel veri tipi ile referans veri tipi arasındaki farklar:
    1- ilkel veri tipleri (primitive types) değerleri doğrudan saklar, referans veri tipleri (reference types) ise değerlerin adreslerini saklar.
    2- ilkel veri tipleri değiştirilemez (immutable), referans veri tipleri değiştirilebilir (mutable).
    3- ilkel veri tipleri kopyalandığında yeni bir kopya oluşturulur, referans veri tipleri kopyalandığında aynı adresi paylaşır.
    4- ilkel veri tipleri bellekte stack'te saklanır, referans veri tipleri heap'te saklanır.

    var // var değişken tanımlamak için kullanılır. Ancak let ve const daha modern ve güvenli bir şekilde değişken tanımlamak için tercih edilir.
    const // const ile tanımlanan bir nesne veya dizinin içeriği değiştirilebilir, sadece referansı değiştirilemez.
        const kullanici = { ad: "Ali", yas: 25 };
        kullanici.yas = 26;     // ✅ İçerik değiştirilebilir
        // kullanici = {};      // ❌ Referans değiştirilemez!   ,
        💡 Altın Kural: Modern JavaScript'te varsayılan olarak const kullan. Değerin değişeceğini biliyorsan let kullan. var'dan kaçın!

    let // let değişken tanımlamak için kullanılır ve değeri değiştirilebilir. Modern JavaScript'te tercih edilen değişken tanımlama yöntemidir.

    typeof // typeof operatörü, bir değişkenin veri türünü döndürür. Örnek: typeof 10 // "number"
    typeof null // "object" olarak döner, çünkü null bir nesne olarak kabul edilir.Null kontrolü için value === null kullanın!
    typeof undefined // "undefined" olarak döner, çünkü undefined bir tanımsız değerdir.

*/



let message = "Merhaba World!"; 
let kullanıcıAdı = {
    isim : "Gökhan Altay",
    yaş : 23,
    şehir : "İstanbul"
}
console.log(message);//* Tarayıcı konsoluna mesajı yazdırır.Sık kullanılan bir yöntemdir. Tarayıcı konsolunu açmak için F12 tuşuna basabilir veya sağ tıklayıp "İncele" seçeneğini seçebilirsiniz.
console.warn(message);//* Tarayıcı konsoluna uyarı mesajı yazdırır. Genellikle hata ayıklama sırasında kullanılır.
console.error(message);//* Tarayıcı konsoluna hata mesajı yazdırır. Genellikle hata ayıklama sırasında kullanılır.  
document.write(message);//* Tarayıcıda sayfa üzerinde mesajı yazdırır. Genellikle test amaçlı kullanılır, ancak üretim ortamında kullanılması önerilmez.
console.table(kullanıcıAdı);//* Tarayıcı konsoluna tablo formatında mesajı yazdırır. Genellikle veri yapıları ve diziler için kullanılır.
window.alert(message);//* Tarayıcıda bir uyarı penceresi açar ve mesajı gösterir. Kullanıcıdan onay almak için kullanılabilir.
