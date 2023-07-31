# Trial for new way of batching sentence transformer, not any faster

for ix in tqdm(range(0, len(data), BATCH_SIZE)):
            # Get the embeddings in batched way
            articles = data[ix : ix + BATCH_SIZE]
            abss = [article["abstract"] for article in articles]
            abss_embs = get_vecs(abss)
            heads = [article["headline"]["main"] for article in articles]
            heads_embs = get_vecs(heads)
            pars = [article["lead_paragraph"] for article in articles]
            pars_embs = get_vecs(pars)
            # Add them to the indexes
            for jx, (abs_emb, head_emb, par_emb) in enumerate(
                zip(abss_embs, heads_embs, pars_embs)
            ):
                abs_ix.add_item(ix + jx, abs_emb)
                head_ix.add_item(ix + jx, head_emb)
                par_ix.add_item(ix + jx, par_emb)
        # Add the article metadata
        for ix, article in enumerate(data):
            meta = schema.Article(
                id=article["_id"],
                month=util.month_to_str(date),
                annoy_ix=ix,
                abstract=article["abstract"],
                headline=article["headline"]["main"],
                lead_paragraph=article["lead_paragraph"],
            )
            dbman.add_article(meta)
        dbman.con.commit()

