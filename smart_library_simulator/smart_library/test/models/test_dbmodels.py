from smart_library.src.models.dbmodels import Fragrance


class TestFragrance:

    def test_fragrance_properties_are_updated_based_on_dictionary_content_even_if_not_existing(self):  # noqa: E501
        # Given
        fragrance = Fragrance(
            fragrance_id="123",
            name="test_fragrance",
            description="test_description",
            cost=1,
            forbidden=True
        )
        content = {
            "name": "new",
            "cost": "42",
            "unkonwn": "unknonwn"
        }

        # When
        fragrance.update(content)

        # Then
        assert fragrance.name == content["name"]
        assert fragrance.unkonwn == content["unkonwn"]
