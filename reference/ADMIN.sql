
CREATE DATABASE credit_card_transaction

CREATE TABLE ADMIN 
(
AdminID INT PRIMARY KEY, 
FirstName VARCHAR(40) NOT NULL,
LastName VARCHAR(40) NOT NULL,
UserName VARCHAR(40) NOT NULL,
PassWord VARCHAR(40) NOT NULL,
Manager CHAR(1) DEFAULT 'N' NOT NULL,
Phone CHAR(10) UNIQUE KEY NOT NULL 
)

INSERT INTO ADMIN (AdminID,FirstName,LastName,UserName,PassWord,Phone) VALUES
	 (1,'Tài','Lê','minhtai123','Taile','0902676011'),
	 (2,'Tiến','Lê','tienlm22416c@st.uel.edu.vn','Tienle22416@','0902676012'),
	 (3,'a','b','c','123','0901111111'),
	 (4,'Thanh','Trần','tranduythanh','1234','0902676010');
