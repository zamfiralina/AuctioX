CREATE OR REPLACE VIEW copy_items as select * from items;

CREATE OR REPLACE TRIGGER delete_item
  INSTEAD OF delete ON copy_items
BEGIN
  delete from TAGS where item_id=:OLD.item_id;
  delete from ITEMS where item_id=:OLD.item_id;
END;