CREATE TABLE public."users"
(
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    PRIMARY KEY (id)
);



CREATE TABLE public.posts
(
    id integer NOT NULL,
    content character varying NOT NULL,
    owner_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id)
        REFERENCES public."users" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);



CREATE TABLE public.comments
(
    id integer NOT NULL,
    content character varying NOT NULL,
    owner_id integer NOT NULL,
    post_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id)
        REFERENCES public."users" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID,
    FOREIGN KEY (post_id)
        REFERENCES public.posts (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);

--data for users table
INSERT INTO users (id, username, password) VALUES (1,'brent','$2b$12$ltfC8LEeg/nli9q3fBNrTemUboDNiYeqzRn7IM/G4OuO4jvj5smTm');
INSERT INTO users (id, username, password) VALUES (2,'neil','$2b$12$dC1tXmT2M8/vn9tfvDa5xuy1warhC26ydf03REiLfUB4V4gDjHLPC');
INSERT INTO users (id, username, password) VALUES (3,'sean','$2b$12$TX09n114Y..jBi/eJpdhp.CobZCbaCpN0R9xNuItIrdsO9gfVclfe');
INSERT INTO users (id, username, password) VALUES (4,'dev','$2b$12$tZj9TvXXJPM.vD5v.dc5L.8fleW1Kh9s5ztjLjQi9s/amKVeJpGYC');
INSERT INTO users (id, username, password) VALUES (5,'test','$2b$12$tZP.6T84HNyOrote9fa9jOUNE5itxX4K2dTvyTrBvmOiABXckIrAC');

--data for posts table
INSERT INTO posts (id,content,owner_id,created_at) VALUES (6,'tester post 1', 5,'2023-01-15 20:43:22.033497+00');
INSERT INTO posts (id,content,owner_id,created_at) VALUES (7,'tester post 2', 5,'2023-01-15 20:43:30.081689+00');

--data for comments table
INSERT INTO comments (id,content, owner_id, post_id, created_at) VALUES (6,'brent''s another commment',1,7,'2023-01-15 21:07:22.445117+00');
INSERT INTO comments (id,content, owner_id, post_id, created_at) VALUES (7,'neil''s this commment',2,7,'2023-01-15 21:07:22.445117+00');
INSERT INTO comments (id,content, owner_id, post_id, created_at) VALUES (8,'neil''s that commment',2,7,'2023-01-15 21:07:22.445117+00');



