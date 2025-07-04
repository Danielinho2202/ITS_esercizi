create table Docente (
	mat integer primary key,
	cognome varchar(100) not null,
	nome varchar(100) not null,
	email varchar(100),
	);
create table Corso (
	codice integer primary key,
	nome varchar(100) not null,
	aula varchar(2)not null,
	)
create table Incarico (
	Docente integer not null,
	Corso integer not null,
	primary key (Docente , Corso),
	foreign key (Docente) references Docente(mat),
	foreign key (Corso) references Corso(codice),
	)