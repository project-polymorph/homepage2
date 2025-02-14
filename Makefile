.PHONY: build clean

build:
	make docs/文档/编年录/新闻报道
	make docs/文档/编年录/学术研究与调查报告
	make docs/文档/编年录/政策法规
	make docs/文档/编年录/综合索引

docs/文档/编年录/新闻报道:
	mkdir -p docs/文档/编年录/新闻报道
	cd docs/文档/编年录 && python ../../../scripts/generate_index.py --config news_query.json --state .news_index_state.json

docs/文档/编年录/学术研究与调查报告:
	mkdir -p docs/文档/编年录/学术研究与调查报告
	cd docs/文档/编年录 && python ../../../scripts/generate_index.py --config paper_query.json --state .paper_index_state.json	

docs/文档/编年录/政策法规:
	cp -R templates/政策法规 docs/文档/编年录/政策法规
	cd docs/文档/编年录 && python ../../../scripts/generate_index.py --config policy_query.json --state .policy_index_state.json

docs/文档/编年录/综合索引:
	mkdir -p docs/文档/编年录/综合索引
	cd docs/文档/编年录 && python ../../../scripts/generate_index.py --config total_query.json --state .total_index_state.json

clean:
	rm -rf docs/文档/编年录/新闻报道
	rm -rf docs/文档/编年录/学术研究与调查报告
	rm -rf docs/文档/编年录/政策法规
	rm -f docs/文档/编年录/.news_index_state.json
	rm -f docs/文档/编年录/.paper_index_state.json
	rm -f docs/文档/编年录/.policy_index_state.json
	rm -f docs/文档/编年录/.total_index_state.json
