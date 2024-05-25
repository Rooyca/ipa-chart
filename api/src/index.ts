import { Hono } from "hono";

type Bindings = {
  DB: D1Database;
};

const app = new Hono<{ Bindings: Bindings }>();

app.get("/char/:type", async (c) => {
  const type = c.req.param("type");
  try {
    let { results } = await c.env.DB.prepare(
      "SELECT * FROM charts WHERE type = ?",
    )
      .bind(type)
      .all();
    return c.json(results);
  } catch (e) {
    return c.json({ err: e.message }, 500);
  }
});

app.get("/char/name/:name", async (c) => {
  const name = c.req.param("name");
  try {
	let { results } = await c.env.DB.prepare(
	  "SELECT * FROM charts WHERE name LIKE ?",
	)
	  .bind("%"+name+"%")
	  .all();
	return c.json(results);
  } catch (e) {
	return c.json({ err: e.message }, 500);
  }
});

export default app;