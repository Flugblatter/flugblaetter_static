import json
from typesense.api_call import ObjectNotFound
from acdh_cfts_pyutils import TYPESENSE_CLIENT as client
import re
# from acdh_tei_pyutils.tei import TeiReader
# from tqdm import tqdm


page_base_url = ""
typesense_collection_name = "flugblaetter_todesurteile"
xml_path = "./data/editions/*.xml"
tei_ns = ""
json_docsindex_path = "./json/documents.json"
json_punishments_path = "./json/punishments.json"


def load_json(path):
    json_data = None
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data


def create_records(punishments_by_id: dict):
    document_records = []
    docindex_json = load_json(json_docsindex_path)
    for id, doc_info in docindex_json.items():
        trial_results = [ punishments_by_id[e_id] for e_id in doc_info["contains_events"] if "trial_result" in e_id ]
        execution = [trial_result for trial_result in trial_results if trial_result["type"] == "execution"]
        if len(execution) == 1:
            execution = execution[0]
        elif len(execution) == 0:
            # z.B.
            # 303_annot_tei/17970000_JohannMüllner-JgnazMenz-GeorgDürnböck-ThomasSchedel.xml 
            #input(f"doc {id} contains no execution")
            pass
        else:
            # z.B.
            # fb_17780827_JohannH_MichaelH
            #input(f"doc {id} contains more then one execution")
            execution = trial_results[-1]
        document_record = {
            "title": doc_info["title"],
            "execution_date" : int(re.sub("-", "", execution["date"][0])) if execution else 17490000,
            "identifier" : doc_info["id"],
            "filename" : doc_info["filename"],
            "fulltext" : doc_info["fulltext"],
        }
        document_records.append(document_record)
    return document_records



    "fb_17391110_JohannK": {
        "sorting_date": 17391110,
        "title": "Todesurteil Johann K.",
        "id": "fb_17391110_JohannK",
        "filename": "fb_17391110_JohannK.xml",
        "contains_persons": [
            {
                "global_id": "pers_fb_17391110_JohannK_d1",
                "forename": "Johann",
                "surname": "K.",
                "birth_element": "<birth xmlns=\"http://www.tei-c.org/ns/1.0\">\n                  <placeName source=\"#pn15\">\n                     <settlement>Wien</settlement>\n                     <country/>\n                  </placeName>\n               </birth>\n               ",
                "death_element": "<death xmlns=\"http://www.tei-c.org/ns/1.0\"/>\n               ",
                "roles": {
                    "fb_17391110_JohannK": "delinquent"
                },
                "sex": "m",
                "age": "22",
                "type": "civil",
                "marriage_status": "unwed",
                "faith": "cath",
                "occupation": [
                    "k. A."
                ],
                "file_identifier": "fb_17391110_JohannK",
                "related_events": [
                    "offence_fb_17391110_JohannK_m1",
                    "offence_fb_17391110_JohannK_m2",
                    "offence_fb_17391110_JohannK_m3",
                    "trial_result_fb_17391110_JohannK_0001"
                ],
                "element": "<person xmlns=\"http://www.tei-c.org/ns/1.0\" role=\"delinquent\" xml:id=\"d1\">\n               <persName source=\"#johannk15\">\n                  <forename>Johann</forename>\n                  <surname>\n                     <abbr>K.</abbr>\n                  </surname>\n               </persName>\n               <birth>\n                  <placeName source=\"#pn15\">\n                     <settlement>Wien</settlement>\n                     <country/>\n                  </placeName>\n               </birth>\n               <death/>\n               <sex value=\"m\" source=\"#tu_15_xTok_000015\"/>\n               <age value=\"2\" source=\"#age15\">22</age>\n               <state type=\"civil\" source=\"#tu_15_xTok_000013\">\n                  <desc>unwed</desc>\n               </state>\n               <faith source=\"#tu_15_xTok_000026\">cath</faith>\n               <occupation>k. A.</occupation>\n               <listEvent type=\"offences\" default=\"false\">\n                  <event type=\"offence\" xml:id=\"m1\">\n                     <desc>\n                        <date>k. A.</date>\n                        <placeName>Wien</placeName>\n                        <trait type=\"typeOfOffence\">\n                           <desc>\n                              <list>\n                                 <item>Diebstahl</item>\n                              </list>\n                           </desc>\n                        </trait>\n                        <desc type=\"summary\">mehrmaliger Diebstahl, Verurteilung zu Zuchthaus,\n                           Deportation nach Raab</desc>\n                     </desc>\n                  </event>\n                  <event type=\"offence\" xml:id=\"m2\">\n                     <desc>\n                        <date>k. A.</date>\n                        <placeName>k. A.</placeName>\n                        <trait type=\"typeOfOffence\">\n                           <desc>\n                              <list>\n                                 <item>Urfehdebruch</item>\n                              </list>\n                           </desc>\n                        </trait>\n                        <desc type=\"summary\">dreimaliger Urfehdebruch</desc>\n                     </desc>\n                  </event>\n                  <event type=\"offence\" xml:id=\"m3\">\n                     <desc>\n                        <date>w&#228;hrend des Arrests</date>\n                        <placeName>Gef&#228;ngnis</placeName>\n                        <trait type=\"toolOfCrime\">\n                           <desc>Marmorstein</desc>\n                        </trait>\n                        <trait type=\"typeOfOffence\">\n                           <desc>\n                              <list>\n                                 <item>Mord</item>\n                              </list>\n                           </desc>\n                        </trait>\n                        <desc>Mord an einem mitarrestierten Geistlichen durch mehrere Schl&#228;ge mit\n                           einem viereckigen Marmorstein auf den Kopf</desc>\n                     </desc>\n                  </event>\n                  <relation type=\"causal\" active=\"#m1\" passive=\"#execution\" name=\"causeForExecution\"/>\n               </listEvent>\n               <event type=\"execution\" xml:id=\"execution\">\n                  <desc>\n                     <date when=\"1739-11-10\" source=\"#date15\">10.11.1739</date>\n                     <placeName>Wienerberg</placeName>\n                     <trait type=\"methodOfExecution\">\n                        <desc>wheel from above</desc>\n                     </trait>\n                  </desc>\n               </event>\n            </person>\n         "
            }
        ],
        "contains_events": [
            "offence_fb_17391110_JohannK_m1",
            "offence_fb_17391110_JohannK_m2",
            "offence_fb_17391110_JohannK_m3",
            "trial_result_fb_17391110_JohannK_0001"
        ],
        "fulltext": "Wohl=verdientes Todtes=Urtheil / Einer Ledigen Manns=Persohn / Nahmens Johann K. Catholischer Religion / und 22. Jahr alt / von hier geb\u00fcrtig / Um weilen derselbe nach verschiedenen begangenen Diebst\u00e4hlen, und dar\u00fcber zu dreymahlen abgeschwornen Urpheden vorhin zwar schon zu zweymahlen in dem Zucht=Hau\u00df abgestraffet / letztens aber anf auf 6. Jahr lang nacher Raab condemniret / inzwischen wegen f\u00fcrwehrender Hungarischen Contagion in allhiesiges Gnaden=Stockhau\u00df verleget worden / allda aber einen mit=verarrestirten Geistlichen mit einem schw\u00e4ren viereckigen Marmorstein um solch seiner 6. J\u00e4hrigen Straff=Zeit zu entgehen / todt geschlagen . Als wird derselbe heute Dienstag den 10. November andern zum Beyspiel auf den hohen Wagen gesetzet / sodann auf den Wienner=Berg zur gew\u00f6hnlichen Richtstatt gef\u00fchrt / allda mit dem Rad von oben herab vom Leben zum Todt hingerichtet / der todte C\u00f6rper aber auf das Rad geflochten werden . NB. Der fernere Jnnhalt seines Verbrechens ist hierinnen zu vernehmen . Wienn / gedruckt bey Johann Baptist Schilgen . Kopfleiste aus stilisierten floralen Ornamenten, horizontal gespiegelt Jnnhalt des Verbrechens dises Maleficantens . Dieser anheutige aufgesetzte Delinquent ist vorhin wegen vielf\u00e4ltigen Diebereyen zu drey unterschiedlichen mahlen criminaliter processiret / zweymahlen mit dem Zucht=Hau\u00df ein und zwey Jahr lang abgestraffet / letzlichen aber auf sechs Jahr lang nacher Raab nebst Hinterlassung einer zum dritten mahl geschwornen Urphed condemniret ; immittels aber wegen f\u00fcrw\u00e4hrender Hungarischen Contagion in allhiesiges Gnaden=Stockhau\u00df verleget worden / daselbst aber um solch seiner sechs j\u00e4hrigen Straff=Zeit zu entgehen / mit einen zu Handen genommenen schw\u00e4ren vierecktigten Marmorstein einen nebst ihme in bemeldter Stockhau\u00df=Gef\u00e4ngnus mit=arrestirten Geistlichen \u00fcber den Kopf nicht nur einen solchen gewaltigen Streich versetzet / da\u00df der Geistliche alsogleich nach der L\u00e4nge zur Erden gesuncken / sondern auch / nachdeme sich solcher annoch in etwas ger\u00fchret / demeselben alsogleich noch zwey andere / oder mehrere Streich ( deren sich diser Ubelth\u00e4ter nicht mehr zu erinderen gewust ) zu den Kopf beygebracht / da\u00df hierauf das h\u00e4ufige Blut hergeschossen / und wiederholter Geistlicher sich nicht mehr im geringsten ger\u00fchet ger\u00fchret / oder beweget / sondern urpl\u00f6tzlich Todtes verblichen . Weh Kopfleiste aus stilisierten floralen Ornamenten, horizontal gespiegelt WEh mir ! du schm\u00e4hlichs Rad hast mir den Todt erkohren ! Du tr\u00fcmmerst meinen Leib ! du forderst herbe Peyn ! Weil ich mit \u00fcbler That Verstand und Witz verlohren / So will ein greulichs Rad des Himmels Rach=Schwerd seyn . O Himmel ! was ist di\u00df ? das Hertz im Leib will brechen / Mein \u00e4ngstigs G'wissen selbst thut mir das Urtheil sprechen . So redt Johann sich an : Ein Mensch von jungen Jahren / Der erst der schn\u00f6den Welt ihr Gl\u00e4ntzen suchen will . Allein : es heist anheut sich mit dem Todte paaren / Und wei\u00dft der Laster=Welt ein gr\u00e4ulichs Schauen=Spil / Dann da die Lasterthat vor Tugend ihm gefallen / Was Wunder ! da\u00df man ihm mit solcher M\u00fcntz thut zahlen . Nun g\u00f6nne Leser mir / sein That hier anzubringen / Jch stell dir einen Wust der Missethaten dar ; Sein Sinn war r\u00fcstig sich nach Dieberey zu schwingen / We\u00dfhalben er auch schon zweymahl gestraffet war / Das Zuchthau\u00df solte ihm ein bessers Leben lehren / Und solches th\u00e4t man auch durch Urphed anbegehren . Da aber selbter doch von dem nicht abgelassen / So wurd zur Arbeit er nach Raab geurthelt ab / Er muste wie zuvor die schw\u00e4ren Bande fassen / Der Kercker war sein Hau\u00df / und \u00f6ffnte ihm das Grab / Er lie\u00df Verzweiflungs=Geist in seinen Hertzen walten / Und macht seim Mit=Gespann das Blut im Leib erkalten . O m\u00f6r= O m\u00f6rderische That ! O schr\u00f6ckliches Beginnen ! Mu\u00df eines andern Blut dir eine K\u00fchlung seyn ? Mu\u00df dein Verzweiflung so / ihr End und Zihl gewinnen ? Dient dir zur Labsaal wohl ein schw\u00e4rer Marmor=Stein ? Von dem ein geistlichs Haupt drey scharffe Wunden zehlet / Durch dessen Schicksaal selbst das edle Leben f\u00e4llet . Wie soll dein Hertze nun vergn\u00fcgte Ruhe finden ? Wann nicht bey GOttes=Thron all Gnad th\u00e4t offen stehn / Und selbe thut dir gwi\u00df das ewig Heyl verk\u00fcnden / Wann du bereuter wirst zu deiner Straffe gehn . Du aber / der di\u00df Blat zu lesen g\u00fcnstig achtest / Gib obacht / da\u00df du nicht des Himmels= Straff verachtest . Totensch\u00e4del in Frontalansicht mit Lorbeer gekr\u00e4nzt, links eine brennende Kerze und eine Sanduhr, rechts eine Distel und eine weitere brennende Kerze, auf horizontal schraffierten Grund, gerahmt",
        "print_date": "k. A.",
        "execution_date": "",
        "execution_methods": [],
        "punishment_methods": [
            [
                "wheel from above"
            ]
        ]
    },

def setup_collection():
    print(f"setting up collection '{typesense_collection_name}'")
    current_schema = {
        "name": typesense_collection_name,
        "enable_nested_fields": True,
        "default_sorting_field": "sorting_date",
        "fields": [
            {"name": "sorting_date", "type": "int32"},
            {"name": "title", "type": "string"},
            {"name": "filename", "type": "string"},
            {"name": "id", "type": "string"},
            {"name": "filename", "type": "string"},
            {"name": "fulltext", "type": "string"},
            {"name": "contains_persons.global_id", "type": "string"},
            {"name": "contains_persons.forename", "type": "string"},
            {"name": "contains_persons.surname", "type": "string"},

        ],
    }
    try:
        client.collections[typesense_collection_name].delete()
        print(f"resetted collection '{typesense_collection_name}'")
    except ObjectNotFound:
        pass
    client.collections.create(current_schema)
    print(f"created collection '{typesense_collection_name}'")

def setup_collection_bak():
    print(f"setting up collection '{typesense_collection_name}'")
    current_schema = {
        "name": typesense_collection_name,
        "enable_nested_fields": False,
        "default_sorting_field": "execution_date",
        "fields": [
            {"name": "execution_date", "type": "int32"},
            {"name": "identifier", "type": "string"},
            {"name": "filename", "type": "string"},
            {"name": "fulltext", "type": "string"},
            {"name": "title", "type": "string"}
        ],
    }
    try:
        client.collections[typesense_collection_name].delete()
        print(f"resetted collection '{typesense_collection_name}'")
    except ObjectNotFound:
        pass
    client.collections.create(current_schema)
    print(f"created collection '{typesense_collection_name}'")


def upload_records(records):
    print(f"uploading '{len(records)}' records")
    setup_collection()
    print(f"uploading to {typesense_collection_name}")
    make_index = client.collections[typesense_collection_name].documents.import_(
        records, {"action": "upsert"}
    )
    errors = [
        msg for msg in make_index if (msg != '"{\\"success\\":true}"' and msg != '""')
    ]
    if errors:
        for err in errors:
            print(err)
    else:
        print("\nno errors")
    print(f'\ndone with indexing "{typesense_collection_name}"')
    return make_index


if __name__ == "__main__":
    punishments_by_id = load_json(json_punishments_path)
    records = create_records(punishments_by_id)
    result = upload_records(records)
