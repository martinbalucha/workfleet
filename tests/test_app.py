import workfleet.application
import workfleet.domain
import workfleet.infrastructure
import workfleet.infrastructure.persistence
import workfleet.web_api
from workfleet import main


def test_layers_import() -> None:
    modules = (
        workfleet.domain,
        workfleet.application,
        workfleet.infrastructure,
        workfleet.infrastructure.persistence,
        workfleet.web_api,
    )
    assert [module.__name__ for module in modules] == [
        "workfleet.domain",
        "workfleet.application",
        "workfleet.infrastructure",
        "workfleet.infrastructure.persistence",
        "workfleet.web_api",
    ]


def test_main_prints_greeting(capsys) -> None:
    main()
    assert capsys.readouterr().out == "Hello from workfleet!\n"
