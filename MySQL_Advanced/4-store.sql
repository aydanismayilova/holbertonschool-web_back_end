--Hər dəfə orders cədvəlinə yeni sifariş əlavə olunanda → avtomatik items.quantity azalsın--
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
