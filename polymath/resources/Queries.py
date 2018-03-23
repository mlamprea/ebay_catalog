SELECT super.CategoryID AS parent,
       sub.CategoryID AS child
FROM Category AS sub
JOIN Category AS super on(super.CategoryID = sub.ParentID)
ORDER BY super.CategoryLevel,
         super.CategoryID ASC;


select CategoryID, CategoryName, CategoryLevel, BestOfferEnabled from Category;
