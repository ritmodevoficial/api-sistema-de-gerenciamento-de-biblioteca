--
-- Dump do banco de dados PostgreSQL
--

-- Dumpado da versão do banco de dados 15.3
-- Dumpado pela versão pg_dump 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Nome: book_types; Tipo: TABELA; Esquema: public; Proprietário: postgres
--

CREATE TABLE public.book_types (
    id integer NOT NULL,
    subject_name character varying
);


ALTER TABLE public.book_types OWNER TO postgres;

--
-- Nome: book_types_id_seq; Tipo: SEQUÊNCIA; Esquema: public; Proprietário: postgres
--

CREATE SEQUENCE public.book_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_types_id_seq OWNER TO postgres;

--
-- Nome: book_types_id_seq; Tipo: SEQUÊNCIA POSSUIDA POR; Esquema: public; Proprietário: postgres
--

ALTER SEQUENCE public.book_types_id_seq OWNED BY public.book_types.id;


--
-- Nome: books; Tipo: TABELA; Esquema: public; Proprietário: postgres
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name character varying,
    author character varying,
    copy_number integer,
    book_type_id integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Nome: books_id_seq; Tipo: SEQUÊNCIA; Esquema: public; Proprietário: postgres
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO postgres;

--
-- Nome: books_id_seq; Tipo: SEQUÊNCIA POSSUIDA POR; Esquema: public; Proprietário: postgres
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Nome: borrows; Tipo: TABELA; Esquema: public; Proprietário: postgres
--

CREATE TABLE public.borrows (
    id integer NOT NULL,
    student_id integer,
    book_id integer
);


ALTER TABLE public.borrows OWNER TO postgres;

--
-- Nome: borrows_id_seq; Tipo: SEQUÊNCIA; Esquema: public; Proprietário: postgres
--

CREATE SEQUENCE public.borrows_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.borrows_id_seq OWNER TO postgres;

--
-- Nome: borrows_id_seq; Tipo: SEQUÊNCIA POSSUIDA POR; Esquema: public; Proprietário: postgres
--

ALTER SEQUENCE public.borrows_id_seq OWNED BY public.borrows.id;


--
-- Nome: students; Tipo: TABELA; Esquema: public; Proprietário: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name character varying,
    department character varying
);


ALTER TABLE public.students OWNER TO postgres;

--
-- Nome: students_id_seq; Tipo: SEQUÊNCIA; Esquema: public; Proprietário: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO postgres;

--
-- Nome: students_id_seq; Tipo: SEQUÊNCIA POSSUIDA POR; Esquema: public; Proprietário: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Nome: book_types id; Tipo: DEFAULT; Esquema: public; Proprietário: postgres
--

ALTER TABLE ONLY public.book_types ALTER COLUMN id SET DEFAULT nextval('public.book_types_id_seq'::regclass);


--
-- Nome: books id; Tipo: DEFAULT; Esquema: public; Proprietário: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Nome: borrows id; Tipo: DEFAULT; Esquema: public; Proprietário: postgres
--

ALTER TABLE ONLY public.borrows ALTER COLUMN id SET DEFAULT nextval('public.borrows_id_seq'::regclass);


--
-- Nome: students id; Tipo: DEFAULT; Esquema: public; Proprietário: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Dados para Nome: book_types; Tipo: DADOS DA TABELA; Esquema: public; Proprietário: postgres
--

COPY public.book_types (id, subject_name) FROM stdin;
1	Matemática
2	Literatura
\.


--
-- Dados para Nome: books; Tipo: DADOS DA TABELA; Esquema: public; Proprietário: postgres
--

COPY public.books (id, name, author, copy_number, book_type_id) FROM stdin;
3	Matemática 101	Mestre da Matemática	10	\N
4	Obras de Shakespeare	William Shakespeare	5	2
1	Armas	Jared Diamond	4	1
\.


--
-- Dados para Nome: borrows; Tipo: DADOS DA TABELA; Esquema: public; Proprietário: postgres
--

COPY public.borrows (id, student_id, book_id) FROM stdin;
5	1	3
6	3	4
\.


--
-- Dados para Nome: students; Tipo: DADOS DA TABELA; Esquema: public; Proprietário: postgres
--

COPY public.students (id, name, department) FROM stdin;
1	João Doe	Ciência da Computação
2	João Doe	Ciência da Computação
3	Jane Doe	Física
\.


--
-- Nome: book_types_id_seq; Tipo: SEQUÊNCIA DEFINIDA; Esquema: public; Proprietário: postgres
--

SELECT pg_catalog.setval('public.book_types_id_seq', 2, true);


--
-- Nome: books_id_seq; Tipo: SEQUÊNCIA DEFINIDA; Esquema: public; Proprietário: postgres
--

SELECT pg_catalog.setval('public.books_id_seq', 4, true);


--
-- Nome: borrows_id_seq; Tipo: SEQUÊNCIA DEFINIDA; Esquema: public; Proprietário: postgres
--

SELECT pg_catalog.setval('public.borrows_id_seq', 6, true);


--
-- Nome: students_id_seq; Tipo : SEQUÊNCIA DEFINIDA ; Esquema : público ; Proprietário :postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 3, true);


--
-- Nome : book_types book_types_pkey ; Tipo : CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.book_types
   ADD CONSTRAINT book_types_pkey PRIMARY KEY (id);


--
-- Nome : books books_pkey ; Tipo : CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.books
   ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Nome : borrows borrows_pkey ; Tipo : CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.borrows
   ADD CONSTRAINT borrows_pkey PRIMARY KEY (id);


--
-- Nome : students students_pkey ; Tipo : CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.students
   ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Nome : ix_book_types_id ; Tipo : ÍNDICE ; Schema : público ; Owner :postgres
--

CREATE INDEX ix_book_types_id ON public.book_types USING btree (id);


--
-- Nome : ix_books_id ; Tipo : ÍNDICE ; Schema : público ; Owner :postgres
--

CREATE INDEX ix_books_id ON public.books USING btree (id);


--
-- Nome : ix_borrows_id ; Tipo : ÍNDICE ; Schema : público ; Owner :postgres
--

CREATE INDEX ix_borrows_id ON public.borrows USING btree (id);


--
-- Nome : ix_students_id ; Tipo : ÍNDICE ; Schema : público ; Owner :postgres
--

CREATE INDEX ix_students_id ON public.students USING btree (id);


--
-- Nome : books books_book_type_id_fkey ; Tipo : FK CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.books
   ADD CONSTRAINT books_book_type_id_fkey FOREIGN KEY (book_type_id) REFERENCES public.book_types(id);


--
-- Nome : borrows borrows_book_id_fkey ; Tipo : FK CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.borrows
   ADD CONSTRAINT borrows_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Nome : borrows borrows_student_id_fkey ; Tipo : FK CONSTRAINT ; Schema : público ; Owner :postgres
--

ALTER TABLE ONLY public.borrows
   ADD CONSTRAINT borrows_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id);


--
-- Dump do banco de dados PostgreSQL completo.
--
