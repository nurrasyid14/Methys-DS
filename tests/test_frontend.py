from methys import Frontend, FrontendBlock, InlineQuery, QueryDialect, native_version


def test_frontend_renders_every_block_type() -> None:
    page = Frontend(title="A & B")
    page.add_html("<main>content</main>")
    page.add_css("main { color: teal; }")
    page.add_javascript("console.log('ready');")

    output = page.render()

    assert "<title>A &amp; B</title>" in output
    assert "<main>content</main>" in output
    assert "main { color: teal; }" in output
    assert "console.log('ready');" in output


def test_blocks_are_public_data_objects() -> None:
    assert FrontendBlock(kind="html", content="<p />").kind == "html"
    assert native_version() == "0.1.0"


def test_inline_queries_preserve_dialect_statement_and_parameters() -> None:
    query = InlineQuery.postgres("SELECT :account_id", {"account_id": 42})
    mongo = InlineQuery.mongodb('{"active": true}')

    assert query.dialect is QueryDialect.POSTGRES
    assert query.parameters == {"account_id": 42}
    assert mongo.dialect is QueryDialect.MONGODB
